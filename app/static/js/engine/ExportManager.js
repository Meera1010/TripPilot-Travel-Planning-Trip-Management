/**
 * High-Resolution Canvas PNG Exporter & Spec Tech Pack Builder
 */
class ExportManager {
  static exportCanvasAsPNG(canvasElement, fileName = 'outfit-design.png') {
    const link = document.createElement('a');
    link.download = fileName;
    link.href = canvasElement.toDataURL('image/png', 1.0);
    link.click();
  }

  static async generateTechPackSpecSheet(designId) {
    try {
      const res = await API.get(`/designs/${designId}`);
      if (!res.success) throw new Error('Failed to load design');

      const techPackData = await API.get(`/costing/${designId}`);
      const specData = await API.get(`/sizing/spec-sheets/${designId}`);

      showToast('Generating factory tech pack PDF spec summary...', 'info');

      // Create printable window
      const printWin = window.open('', '_blank');
      printWin.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
          <title>Tech Pack - ${res.data.title}</title>
          <style>
            body { font-family: Arial, sans-serif; padding: 30px; color: #111; }
            h1 { color: #d90429; border-bottom: 2px solid #d90429; padding-bottom: 8px; }
            .header-table { width: 100%; margin-bottom: 20px; border-collapse: collapse; }
            .header-table td { padding: 8px; border: 1px solid #ddd; }
            .section-title { background: #f0f0f0; padding: 8px; margin-top: 24px; font-weight: bold; }
            table { width: 100%; border-collapse: collapse; margin-top: 12px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background: #fafafa; }
          </style>
        </head>
        <body>
          <h1>STYLEFORGE ATELIER - TECHNICAL SPECIFICATION PACK</h1>
          <table class="header-table">
            <tr>
              <td><strong>Garment Title:</strong> ${res.data.title}</td>
              <td><strong>Category:</strong> ${res.data.category.toUpperCase()}</td>
            </tr>
            <tr>
              <td><strong>Designer:</strong> ${res.data.author_name}</td>
              <td><strong>Collection:</strong> ${res.data.collection_name || 'Standard'}</td>
            </tr>
          </table>

          <div class="section-title">1. BILL OF MATERIALS (BOM) & COSTING</div>
          <table>
            <thead>
              <tr><th>Item Type</th><th>Description</th><th>Qty</th><th>Unit Cost</th><th>Total Cost</th></tr>
            </thead>
            <tbody>
              ${(techPackData.data.items || []).map(i => `
                <tr>
                  <td>${i.item_type.toUpperCase()}</td>
                  <td>${i.item_name}</td>
                  <td>${i.quantity} ${i.unit_of_measure}</td>
                  <td>$${i.unit_cost.toFixed(2)}</td>
                  <td>$${i.total_cost.toFixed(2)}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>

          <div class="section-title">2. POINTS OF MEASURE (POM) & GRADING SPEC</div>
          <p><strong>Sample Size:</strong> ${specData.data.sample_size || 'M'}</p>
          <p><strong>Seam Allowance:</strong> ${specData.data.seam_allowance || '0.5" standard'}</p>

          <script>
            window.onload = function() { window.print(); };
          </script>
        </body>
        </html>
      `);
      printWin.document.close();
    } catch (err) {
      showToast('Error generating tech pack: ' + err.message, 'error');
    }
  }
}
