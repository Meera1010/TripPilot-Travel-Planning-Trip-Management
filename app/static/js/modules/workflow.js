/**
 * Approval Workflow Pipeline Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('workflow-wrapper');
  if (!container) return;

  const urlParams = new URLSearchParams(window.location.search);
  const designId = urlParams.get('id') || 1;

  loadWorkflow(designId);
});

async function loadWorkflow(designId) {
  try {
    const res = await API.get(`/workflows/${designId}`);
    if (res.success && res.data) {
      renderWorkflow(res.data);
    }
  } catch (err) {
    console.error('Error loading workflow:', err);
  }
}

function renderWorkflow(wf) {
  document.getElementById('wf-design-title').textContent = wf.design_title;
  document.getElementById('wf-status-badge').className = `badge badge-${wf.status}`;
  document.getElementById('wf-status-badge').textContent = wf.status.toUpperCase();

  const stepsContainer = document.getElementById('wf-steps-list');
  if (stepsContainer && wf.steps) {
    stepsContainer.innerHTML = wf.steps.map(s => `
      <div class="card" style="margin-bottom:16px;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <div>
            <span style="font-size:0.8rem;color:var(--text-muted);">Step ${s.step_number}</span>
            <h4 style="font-size:1.05rem;font-weight:600;">${s.step_name}</h4>
          </div>
          <span class="badge badge-${s.status}">${s.status}</span>
        </div>
        ${s.comments ? `<p style="font-size:0.85rem;color:var(--text-secondary);margin-top:8px;font-style:italic;">"${s.comments}"</p>` : ''}
        <div style="margin-top:14px;display:flex;gap:10px;">
          <button class="btn btn-sm btn-primary" onclick="processStepAction(${s.id}, 'approve')">Approve</button>
          <button class="btn btn-sm btn-outline" onclick="processStepAction(${s.id}, 'reject')">Reject</button>
        </div>
      </div>
    `).join('');
  }
}

async function processStepAction(stepId, action) {
  const comments = prompt(`Enter optional review comments for ${action}:`) || '';
  try {
    const res = await API.post('/workflows/step/action', { step_id: stepId, action: action, comments: comments });
    if (res.success) {
      showToast(`Workflow step ${action}d!`, 'success');
      renderWorkflow(res.data);
    }
  } catch (err) {
    showToast('Error executing approval action', 'error');
  }
}
