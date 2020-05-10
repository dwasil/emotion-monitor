from Xlib import display

disp = display.Display()
res = disp.screen().root.query_pointer()
window = res.child
print(window.id)
gc = window.create_gc()
window.draw_text(gc, 200, 200, str.encode(str(window.id)))  # changed the coords more towards the center
window.rectangle(gc, 100, 100, 100, 100, onerror=None)
disp.flush()
