/**
 * Garment Production Cost Calculator Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const costingContainer = document.getElementById('costing-wrapper');
  if (!costingContainer) return;

  const urlParams = new URLSearchParams(window.location.search);
  const designId = urlParams.get('id') || 1;

  loadCostingSheet(designId);

  const addItemForm = document.getElementById('add-cost-item-form');
  if (addItemForm) {
    addItemForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        item_type: addItemForm.item_type.value,
        item_name: addItemForm.item_name.value,
        quantity: parseFloat(addItemForm.quantity.value),
        unit_cost: parseFloat(addItemForm.unit_cost.value),
        waste_allowance_pct: parseFloat(addItemForm.waste_allowance_pct.value)
      };

      try {
        const res = await API.post(`/costing/${designId}/items`, payload);
        if (res.success) {
          showToast('BOM cost item added', 'success');
          closeModal('modal-add-cost-item');
          renderCostingSheet(res.data);
        }
      } catch (err) {
        showToast('Error adding cost item', 'error');
      }
    });
  }
});

async function loadCostingSheet(designId) {
  try {
    const res = await API.get(`/costing/${designId}`);
    if (res.success && res.data) {
      renderCostingSheet(res.data);
    }
  } catch (err) {
    console.error('Error loading costing sheet:', err);
  }
}

function renderCostingSheet(data) {
  document.getElementById('cost-fabric-sum').textContent = formatCurrency(data.total_fabric_cost);
  document.getElementById('cost-material-sum').textContent = formatCurrency(data.total_material_cost);
  document.getElementById('cost-labor-sum').textContent = formatCurrency(data.total_labor_cost);
  document.getElementById('cost-total-est').textContent = formatCurrency(data.estimated_cost);
  document.getElementById('cost-wholesale').textContent = formatCurrency(data.wholesale_price);
  document.getElementById('cost-retail').textContent = formatCurrency(data.retail_price);
  document.getElementById('cost-margin').textContent = `${data.calculated_margin_pct}%`;

  const tbody = document.getElementById('cost-items-tbody');
  if (tbody && data.items) {
    tbody.innerHTML = data.items.map(item => `
      <tr>
        <td><span class="badge badge-approved">${item.item_type.toUpperCase()}</span></td>
        <td><strong>${item.item_name}</strong></td>
        <td>${item.quantity} ${item.unit_of_measure}</td>
        <td>$${item.unit_cost.toFixed(2)}</td>
        <td>${item.waste_allowance_pct}%</td>
        <td style="font-weight:700;">$${item.total_cost.toFixed(2)}</td>
      </tr>
    `).join('');
  }
}
