/**
 * Fabric & Materials Inventory Module Controller
 */
document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('fabric-inventory-table');
  if (!container) return;

  loadInventory();

  const addForm = document.getElementById('add-fabric-form');
  if (addForm) {
    addForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        name: addForm.name.value,
        fabric_type: addForm.fabric_type.value,
        composition: addForm.composition.value,
        color_name: addForm.color_name.value,
        color_hex: addForm.color_hex.value,
        unit_price: parseFloat(addForm.unit_price.value),
        current_stock: parseFloat(addForm.current_stock.value),
        minimum_stock: parseFloat(addForm.minimum_stock.value)
      };

      try {
        const res = await API.post('/inventory/fabrics', payload);
        if (res.success) {
          showToast('Fabric added to inventory', 'success');
          closeModal('modal-add-fabric');
          loadInventory();
        }
      } catch (err) {
        showToast('Error adding fabric', 'error');
      }
    });
  }
});

async function loadInventory() {
  const tableBody = document.getElementById('fabric-table-body');
  if (!tableBody) return;

  try {
    const res = await API.get('/inventory/fabrics');
    if (res.success && res.data.items) {
      tableBody.innerHTML = res.data.items.map(f => `
        <tr>
          <td>
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="width:20px;height:20px;border-radius:4px;background:${f.color_hex};border:1px solid var(--border-color);"></span>
              <div>
                <strong style="display:block;">${f.name}</strong>
                <span style="font-size:0.75rem;color:var(--text-muted);">${f.code}</span>
              </div>
            </div>
          </td>
          <td>${f.fabric_type.toUpperCase()}</td>
          <td>${f.composition}</td>
          <td>$${f.unit_price.toFixed(2)}/m</td>
          <td>
            <span style="font-weight:700;color:${f.is_low_stock ? 'var(--accent-primary)' : 'var(--text-primary)'}">
              ${f.current_stock} m
            </span>
            ${f.is_low_stock ? '<span class="badge badge-rejected" style="margin-left:6px;">LOW STOCK</span>' : ''}
          </td>
          <td>${f.supplier_name}</td>
        </tr>
      `).join('');
    }
  } catch (err) {
    console.error('Error loading inventory:', err);
  }
}
