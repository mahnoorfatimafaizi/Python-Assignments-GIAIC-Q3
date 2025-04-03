import tkinter as tk
from typing import List, Tuple

CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40  
ERASER_SIZE: int = 20  

def main():

    window: tk.Tk = tk.Tk()
    window.title("Eraser Canvas")
    canvas: tk.Canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="gray")
    canvas.pack()
    
    cells: List[int] = []
    for row in range(CANVAS_HEIGHT // CELL_SIZE):  
        for col in range(CANVAS_WIDTH // CELL_SIZE):  
            x1: int = col * CELL_SIZE
            y1: int = row * CELL_SIZE
            x2: int = x1 + CELL_SIZE
            y2: int = y1 + CELL_SIZE
            cell_id: int = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            cells.append(cell_id)
    
    eraser: int = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="red")
    
    def move_eraser(event: tk.Event) -> None:

        x: int = event.x - ERASER_SIZE // 2  
        y: int = event.y - ERASER_SIZE // 2
        canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        
        eraser_coords: Tuple[float, float, float, float] = canvas.coords(eraser)
        for cell_id in cells:
            cell_coords: Tuple[float, float, float, float] = canvas.coords(cell_id)
            if overlap(eraser_coords, cell_coords):
                canvas.itemconfig(cell_id, fill="white")
    
    def overlap(rect1: Tuple[float, float, float, float], rect2: Tuple[float, float, float, float]) -> bool:

        x1, y1, x2, y2 = rect1  
        x3, y3, x4, y4 = rect2  
        return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)
    
    canvas.bind("<Motion>", move_eraser)
    
    window.mainloop()

if __name__ == "__main__":
    main()