/**
 * Undo & Redo Canvas State History Stack Manager
 */
class UndoManager {
  constructor(maxSize = 30) {
    this.maxSize = maxSize;
    this.undoStack = [];
    this.redoStack = [];
  }

  saveState(stateJSON) {
    this.undoStack.push(JSON.stringify(stateJSON));
    if (this.undoStack.length > this.maxSize) {
      this.undoStack.shift();
    }
    this.redoStack = []; // Clear redo stack on new action
  }

  undo(currentStateJSON) {
    if (this.undoStack.length === 0) return null;
    this.redoStack.push(JSON.stringify(currentStateJSON));
    const previousState = this.undoStack.pop();
    return JSON.parse(previousState);
  }

  redo(currentStateJSON) {
    if (this.redoStack.length === 0) return null;
    this.undoStack.push(JSON.stringify(currentStateJSON));
    const nextState = this.redoStack.pop();
    return JSON.parse(nextState);
  }

  canUndo() {
    return this.undoStack.length > 0;
  }

  canRedo() {
    return this.redoStack.length > 0;
  }
}
