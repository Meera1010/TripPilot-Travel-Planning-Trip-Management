/**
 * Canvas Studio Layer Class representing Garments, Accessories, Textures, and Patterns
 */
class Layer {
  constructor(config = {}) {
    this.id = config.id || `layer_${Date.now()}_${Math.floor(Math.random()*1000)}`;
    this.type = config.type || 'garment'; // garment, accessory, pattern, text, shape
    this.label = config.label || 'New Layer';
    this.visible = config.visible !== undefined ? config.visible : true;
    this.locked = config.locked || false;
    this.opacity = config.opacity !== undefined ? config.opacity : 1.0;
    this.blendMode = config.blendMode || 'source-over';

    // Transformations
    this.x = config.x || 200;
    this.y = config.y || 250;
    this.width = config.width || 400;
    this.height = config.height || 600;
    this.scaleX = config.scaleX || 1.0;
    this.scaleY = config.scaleY || 1.0;
    this.rotation = config.rotation || 0; // degrees

    // Styling & Content
    this.color = config.color || '#e63946';
    this.patternType = config.patternType || 'solid';
    this.textureUrl = config.textureUrl || '';
    this.svgPath = config.svgPath || '';
    this.subcomponents = config.subcomponents || [];
  }

  getBounds() {
    const w = this.width * this.scaleX;
    const h = this.height * this.scaleY;
    return {
      x: this.x,
      y: this.y,
      width: w,
      height: h,
      cx: this.x + w / 2,
      cy: this.y + h / 2
    };
  }

  containsPoint(px, py) {
    const bounds = this.getBounds();
    return (
      px >= bounds.x &&
      px <= bounds.x + bounds.width &&
      py >= bounds.y &&
      py <= bounds.y + bounds.height
    );
  }

  toJSON() {
    return {
      id: this.id,
      type: this.type,
      label: this.label,
      visible: this.visible,
      locked: this.locked,
      opacity: this.opacity,
      blendMode: this.blendMode,
      x: this.x,
      y: this.y,
      width: this.width,
      height: this.height,
      scaleX: this.scaleX,
      scaleY: this.scaleY,
      rotation: this.rotation,
      color: this.color,
      patternType: this.patternType,
      textureUrl: this.textureUrl,
      svgPath: this.svgPath,
      subcomponents: this.subcomponents
    };
  }
}
