/**
 * 历史上的今天 - 前端交互逻辑
 */

// DOM元素
const dateInput = document.getElementById('dateInput');
const todayBtn = document.getElementById('todayBtn');
const currentDateDisplay = document.getElementById('currentDate');
const eventsContainer = document.getElementById('eventsContainer');
const loadingIndicator = document.getElementById('loadingIndicator');
const errorToast = document.getElementById('errorToast');
const errorMessage = document.getElementById('errorMessage');

// 初始化
document.addEventListener('DOMContentLoaded', function() {
    // 设置日期选择器为今天
    dateInput.value = getCurrentDate();

    // 监听日期选择器变化
    dateInput.addEventListener('change', handleDateChange);

    // 监听"今天"按钮点击
    todayBtn.addEventListener('click', handleTodayClick);
});

/**
 * 处理日期选择变化
 */
async function handleDateChange() {
    const selectedDate = dateInput.value;
    if (!selectedDate) {
        return;
    }

    const date = new Date(selectedDate);
    const month = date.getMonth() + 1;
    const day = date.getDate();

    // 更新当前日期显示
    currentDateDisplay.textContent = formatDate(selectedDate);

    // 获取并显示历史事件
    await fetchAndDisplayEvents(month, day);
}

/**
 * 处理"今天"按钮点击
 */
function handleTodayClick() {
    dateInput.value = getCurrentDate();
    handleDateChange();
}

/**
 * 获取并显示历史事件
 */
async function fetchAndDisplayEvents(month, day) {
    try {
        // 显示加载状态
        showLoading();

        // 调用API获取数据
        const response = await fetch(`/api/events?month=${month}&day=${day}`);

        if (!response.ok) {
            throw new Error('获取数据失败');
        }

        const result = await response.json();

        // 隐藏加载状态
        hideLoading();

        // 检查返回结果
        if (result.success && result.data) {
            displayEvents(result.data);
        } else {
            showError(result.error || '未找到历史事件');
            displayEmptyState();
        }

    } catch (error) {
        console.error('获取历史事件失败:', error);
        hideLoading();
        showError('获取历史事件失败，请稍后重试');
        displayEmptyState();
    }
}

/**
 * 显示历史事件列表
 */
function displayEvents(events) {
    if (!events || events.length === 0) {
        displayEmptyState();
        return;
    }

    // 构建事件卡片HTML
    const eventsHTML = events.map(event => `
        <div class="event-card">
            <div class="event-year">
                ${event.year}年
            </div>
            <div class="event-content">
                <h3 class="event-title">${escapeHtml(event.title)}</h3>
                ${event.desc ? `<p class="event-desc">${escapeHtml(event.desc)}</p>` : ''}
            </div>
        </div>
    `).join('');

    eventsContainer.innerHTML = eventsHTML;
}

/**
 * 显示空状态
 */
function displayEmptyState() {
    eventsContainer.innerHTML = `
        <div class="empty-state">
            <i class="fas fa-search"></i>
            <p>该日期暂无历史事件记录</p>
        </div>
    `;
}

/**
 * 显示加载状态
 */
function showLoading() {
    loadingIndicator.classList.add('active');
    eventsContainer.style.opacity = '0.5';
}

/**
 * 隐藏加载状态
 */
function hideLoading() {
    loadingIndicator.classList.remove('active');
    eventsContainer.style.opacity = '1';
}

/**
 * 显示错误提示
 */
function showError(message) {
    errorMessage.textContent = message;
    errorToast.classList.add('active');

    // 3秒后自动隐藏
    setTimeout(() => {
        errorToast.classList.remove('active');
    }, 3000);
}

/**
 * 转义HTML特殊字符，防止XSS攻击
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * 获取当前日期（格式：YYYY-MM-DD）
 */
function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

/**
 * 格式化日期显示（格式：M月D日）
 */
function formatDate(dateStr) {
    const date = new Date(dateStr);
    const month = date.getMonth() + 1;
    const day = date.getDate();
    return `${month}月${day}日`;
}
