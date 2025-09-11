// Custom JavaScript for Project Admin Interface

document.addEventListener('DOMContentLoaded', function() {
    initProjectAdmin();
});

function initProjectAdmin() {
    initBulkActions();
    initQuickActions();
    initDashboardWidgets();
    initFilters();
    initProjectStatusUpdates();
    initWorkflowIntegration();
}

// Bulk Actions Functionality
function initBulkActions() {
    const checkboxes = document.querySelectorAll('.project-checkbox');
    const bulkActionsContainer = document.querySelector('.project-bulk-actions');
    const selectAllCheckbox = document.querySelector('#select-all-projects');
    
    if (!checkboxes.length || !bulkActionsContainer) return;
    
    // Handle individual checkbox changes
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            updateBulkActionsVisibility();
            updateSelectAllState();
        });
    });
    
    // Handle select all checkbox
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            checkboxes.forEach(checkbox => {
                checkbox.checked = this.checked;
            });
            updateBulkActionsVisibility();
        });
    }
    
    // Bulk action buttons
    initBulkActionButtons();
}

function updateBulkActionsVisibility() {
    const selectedCount = document.querySelectorAll('.project-checkbox:checked').length;
    const bulkActionsContainer = document.querySelector('.project-bulk-actions');
    const selectedCountDisplay = document.querySelector('.selected-count');
    
    if (selectedCount > 0) {
        bulkActionsContainer.classList.add('active');
        if (selectedCountDisplay) {
            selectedCountDisplay.textContent = selectedCount;
        }
    } else {
        bulkActionsContainer.classList.remove('active');
    }
}

function updateSelectAllState() {
    const checkboxes = document.querySelectorAll('.project-checkbox');
    const selectAllCheckbox = document.querySelector('#select-all-projects');
    
    if (!selectAllCheckbox || !checkboxes.length) return;
    
    const checkedCount = document.querySelectorAll('.project-checkbox:checked').length;
    
    if (checkedCount === 0) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = false;
    } else if (checkedCount === checkboxes.length) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = true;
    } else {
        selectAllCheckbox.indeterminate = true;
    }
}

function initBulkActionButtons() {
    // Status change button
    const statusChangeBtn = document.querySelector('#bulk-status-change');
    if (statusChangeBtn) {
        statusChangeBtn.addEventListener('click', function() {
            showBulkStatusModal();
        });
    }
    
    // Priority change button
    const priorityChangeBtn = document.querySelector('#bulk-priority-change');
    if (priorityChangeBtn) {
        priorityChangeBtn.addEventListener('click', function() {
            showBulkPriorityModal();
        });
    }
    
    // Collection change button
    const collectionChangeBtn = document.querySelector('#bulk-collection-change');
    if (collectionChangeBtn) {
        collectionChangeBtn.addEventListener('click', function() {
            showBulkCollectionModal();
        });
    }
    
    // Featured toggle button
    const featuredToggleBtn = document.querySelector('#bulk-featured-toggle');
    if (featuredToggleBtn) {
        featuredToggleBtn.addEventListener('click', function() {
            performBulkFeaturedToggle();
        });
    }
}

// Quick Actions for individual projects
function initQuickActions() {
    const quickCompleteButtons = document.querySelectorAll('.quick-complete-btn');
    quickCompleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const projectId = this.dataset.projectId;
            quickCompleteProject(projectId);
        });
    });
    
    const quickStatusButtons = document.querySelectorAll('.quick-status-btn');
    quickStatusButtons.forEach(button => {
        button.addEventListener('change', function() {
            const projectId = this.dataset.projectId;
            const newStatus = this.value;
            updateProjectStatus(projectId, newStatus);
        });
    });
    
    const quickPriorityButtons = document.querySelectorAll('.quick-priority-btn');
    quickPriorityButtons.forEach(button => {
        button.addEventListener('change', function() {
            const projectId = this.dataset.projectId;
            const newPriority = this.value;
            updateProjectPriority(projectId, newPriority);
        });
    });
}

// Dashboard Widget Functionality
function initDashboardWidgets() {
    initChartWidgets();
    initRefreshableWidgets();
    initExpandableWidgets();
}

function initChartWidgets() {
    // Simple chart creation for status distribution
    const statusCharts = document.querySelectorAll('.project-status-chart');
    statusCharts.forEach(chart => {
        createStatusChart(chart);
    });
}

function createStatusChart(container) {
    const data = JSON.parse(container.dataset.chartData || '[]');
    
    // Create simple bar chart with CSS
    const chartHtml = data.map(item => `
        <div class="chart-bar" style="width: ${item.percentage}%; background-color: ${item.color}">
            <span class="chart-label">${item.label}: ${item.value}</span>
        </div>
    `).join('');
    
    container.innerHTML = chartHtml;
}

function initRefreshableWidgets() {
    const refreshButtons = document.querySelectorAll('.widget-refresh-btn');
    refreshButtons.forEach(button => {
        button.addEventListener('click', function() {
            const widgetType = this.dataset.widget;
            refreshWidget(widgetType);
        });
    });
    
    // Auto-refresh every 5 minutes
    setInterval(function() {
        refreshAllWidgets();
    }, 300000);
}

function refreshWidget(widgetType) {
    const widget = document.querySelector(`[data-widget="${widgetType}"]`);
    if (!widget) return;
    
    widget.classList.add('project-loading');
    
    fetch(`/admin/projects/ajax/dashboard-data/?widget=${widgetType}`)
        .then(response => response.json())
        .then(data => {
            updateWidgetContent(widgetType, data);
        })
        .catch(error => {
            console.error('Error refreshing widget:', error);
        })
        .finally(() => {
            widget.classList.remove('project-loading');
        });
}

// Filter Functionality
function initFilters() {
    const filterForm = document.querySelector('.project-filter-form');
    if (!filterForm) return;
    
    // Auto-submit form when filters change
    const filterInputs = filterForm.querySelectorAll('select, input[type="text"], input[type="date"]');
    filterInputs.forEach(input => {
        input.addEventListener('change', function() {
            debounce(submitFilterForm, 500)();
        });
    });
    
    // Clear filters button
    const clearFiltersBtn = document.querySelector('#clear-filters');
    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', function() {
            clearAllFilters();
        });
    }
    
    // Save filter preset button
    const savePresetBtn = document.querySelector('#save-filter-preset');
    if (savePresetBtn) {
        savePresetBtn.addEventListener('click', function() {
            saveFilterPreset();
        });
    }
}

function submitFilterForm() {
    const filterForm = document.querySelector('.project-filter-form');
    if (filterForm) {
        filterForm.submit();
    }
}

function clearAllFilters() {
    const filterForm = document.querySelector('.project-filter-form');
    if (!filterForm) return;
    
    filterForm.querySelectorAll('select').forEach(select => {
        select.selectedIndex = 0;
    });
    
    filterForm.querySelectorAll('input[type="text"], input[type="date"]').forEach(input => {
        input.value = '';
    });
    
    filterForm.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
        checkbox.checked = false;
    });
    
    submitFilterForm();
}

// AJAX Project Status Updates
function initProjectStatusUpdates() {
    // Already handled in initQuickActions
}

function updateProjectStatus(projectId, newStatus) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch('/admin/projects/ajax/status-update/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `project_id=${projectId}&status=${newStatus}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            // Update UI to reflect the change
            updateProjectStatusUI(projectId, newStatus);
        } else {
            showNotification(data.error || 'Fejl ved opdatering', 'error');
        }
    })
    .catch(error => {
        console.error('Error updating project status:', error);
        showNotification('Netværksfejl ved opdatering', 'error');
    });
}

function updateProjectPriority(projectId, newPriority) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch('/admin/projects/ajax/priority-update/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `project_id=${projectId}&priority=${newPriority}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showNotification(data.message, 'success');
            // Update UI to reflect the change
            updateProjectPriorityUI(projectId, newPriority);
        } else {
            showNotification(data.error || 'Fejl ved opdatering', 'error');
        }
    })
    .catch(error => {
        console.error('Error updating project priority:', error);
        showNotification('Netværksfejl ved opdatering', 'error');
    });
}

function quickCompleteProject(projectId) {
    if (!confirm('Er du sikker på at du vil markere dette projekt som færdigt?')) {
        return;
    }
    
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    fetch(`/admin/projects/quick-complete/${projectId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        if (response.ok) {
            showNotification('Projekt markeret som færdigt', 'success');
            // Refresh the page or update UI
            setTimeout(() => location.reload(), 1000);
        } else {
            showNotification('Fejl ved opdatering', 'error');
        }
    })
    .catch(error => {
        console.error('Error completing project:', error);
        showNotification('Netværksfejl ved opdatering', 'error');
    });
}

// Workflow Integration
function initWorkflowIntegration() {
    const workflowButtons = document.querySelectorAll('.workflow-action-btn');
    workflowButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const action = this.dataset.action;
            const workflowStateId = this.dataset.workflowStateId;
            handleWorkflowAction(action, workflowStateId);
        });
    });
}

function handleWorkflowAction(action, workflowStateId) {
    // This would integrate with Wagtail's workflow system
    console.log('Workflow action:', action, 'for state:', workflowStateId);
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button class="notification-close">&times;</button>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 12px 20px;
        border-radius: 4px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 10000;
        max-width: 400px;
        color: white;
        background-color: ${type === 'success' ? '#22c55e' : type === 'error' ? '#ef4444' : '#3b82f6'};
        animation: slideIn 0.3s ease;
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Handle close button
    notification.querySelector('.notification-close').addEventListener('click', function() {
        notification.remove();
    });
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

function updateProjectStatusUI(projectId, newStatus) {
    const statusElements = document.querySelectorAll(`[data-project-id="${projectId}"] .project-status`);
    statusElements.forEach(element => {
        element.className = `project-status project-status-${newStatus}`;
        element.textContent = getStatusDisplayName(newStatus);
    });
}

function updateProjectPriorityUI(projectId, newPriority) {
    const priorityElements = document.querySelectorAll(`[data-project-id="${projectId}"] .project-priority`);
    priorityElements.forEach(element => {
        element.className = `project-priority project-priority-${newPriority}`;
        element.textContent = getPriorityDisplayName(newPriority);
    });
}

function getStatusDisplayName(status) {
    const statusNames = {
        'planning': 'Planlægning',
        'in_progress': 'I gang',
        'completed': 'Færdig',
        'on_hold': 'På pause',
        'cancelled': 'Annulleret'
    };
    return statusNames[status] || status;
}

function getPriorityDisplayName(priority) {
    const priorityNames = {
        'low': 'Lav',
        'medium': 'Medium',
        'high': 'Høj',
        'urgent': 'Akut'
    };
    return priorityNames[priority] || priority;
}

// Bulk Action Modals
function showBulkStatusModal() {
    const selectedProjects = getSelectedProjects();
    if (selectedProjects.length === 0) return;
    
    const modal = createModal('Ændre Status for Flere Projekter', `
        <form id="bulk-status-form">
            <div class="form-group">
                <label for="bulk-new-status">Ny status:</label>
                <select id="bulk-new-status" name="status" class="form-control">
                    <option value="planning">Planlægning</option>
                    <option value="in_progress">I gang</option>
                    <option value="completed">Færdig</option>
                    <option value="on_hold">På pause</option>
                    <option value="cancelled">Annulleret</option>
                </select>
            </div>
            <p>Dette vil påvirke ${selectedProjects.length} projekter.</p>
        </form>
    `, 'Opdater Status');
    
    modal.querySelector('.modal-confirm').addEventListener('click', function() {
        performBulkStatusChange();
    });
}

function showBulkPriorityModal() {
    const selectedProjects = getSelectedProjects();
    if (selectedProjects.length === 0) return;
    
    const modal = createModal('Ændre Prioritet for Flere Projekter', `
        <form id="bulk-priority-form">
            <div class="form-group">
                <label for="bulk-new-priority">Ny prioritet:</label>
                <select id="bulk-new-priority" name="priority" class="form-control">
                    <option value="low">Lav</option>
                    <option value="medium">Medium</option>
                    <option value="high">Høj</option>
                    <option value="urgent">Akut</option>
                </select>
            </div>
            <p>Dette vil påvirke ${selectedProjects.length} projekter.</p>
        </form>
    `, 'Opdater Prioritet');
    
    modal.querySelector('.modal-confirm').addEventListener('click', function() {
        performBulkPriorityChange();
    });
}

function createModal(title, content, confirmText) {
    const modal = document.createElement('div');
    modal.className = 'modal-overlay';
    modal.innerHTML = `
        <div class="modal">
            <div class="modal-header">
                <h3>${title}</h3>
                <button class="modal-close">&times;</button>
            </div>
            <div class="modal-body">
                ${content}
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary modal-cancel">Annuller</button>
                <button class="btn btn-primary modal-confirm">${confirmText}</button>
            </div>
        </div>
    `;
    
    // Add styles
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 10001;
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    const modalContent = modal.querySelector('.modal');
    modalContent.style.cssText = `
        background: white;
        border-radius: 8px;
        max-width: 500px;
        width: 90%;
        max-height: 80%;
        overflow-y: auto;
    `;
    
    document.body.appendChild(modal);
    
    // Handle close events
    modal.querySelector('.modal-close').addEventListener('click', () => modal.remove());
    modal.querySelector('.modal-cancel').addEventListener('click', () => modal.remove());
    modal.addEventListener('click', function(e) {
        if (e.target === modal) modal.remove();
    });
    
    return modal;
}

function getSelectedProjects() {
    const checkboxes = document.querySelectorAll('.project-checkbox:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Add CSS animation for notifications
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
`;
document.head.appendChild(style);