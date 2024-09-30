import pygame as p, Quartz as q, sys as s, time as t
from PIL import Image as i

def b_i():
    et = q.CGEventTapCreate(
        q.kCGSessionEventTap, 
        q.kCGHeadInsertEventTap, 
        q.kCGEventTapOptionDefault, 
        q.kCGEventMaskForAllEvents,
        lambda pr, t, e, rc: None, None)
    if et:
        rls = q.CFMachPortCreateRunLoopSource(None, et, 0)
        q.CFRunLoopAddSource(q.CFRunLoopGetCurrent(), rls, q.kCFRunLoopCommonModes)
        q.CGEventTapEnable(et, True)
    q.CGDisplayHideCursor(q.CGMainDisplayID())

def u_i():
    q.CGDisplayShowCursor(q.CGMainDisplayID())

def d_i_w_f_i(img_p, t_w):
    p.init()
    sc_info = p.display.Info()
    sc_w, sc_h = sc_info.current_w, sc_info.current_h
    sc = p.display.set_mode((sc_w, sc_h), p.FULLSCREEN)
    p.display.set_caption('L')

    img = i.open(img_p)
    img = img.resize((sc_w, sc_h), i.LANCZOS)
    img = img.convert("RGB")
    md = img.mode
    sz = img.size
    dt = img.tobytes()
    srf = p.image.fromstring(dt, sz, md)

    b_i()
    t_wd = ""
    r = True
    idle = False
    last_mouse_pos = p.mouse.get_pos()
    idle_time = 0

    while r:
        mouse_pos = p.mouse.get_pos()
        if mouse_pos != last_mouse_pos:
            idle = False
        else:
            idle_time += p.time.get_ticks() / 1000.0

        last_mouse_pos = mouse_pos

        if idle_time >= idle_limit:
            idle = True

        if idle:
        else:

        p.display.update()

        for ev in p.event.get():
            if ev.type == p.QUIT:
                p.quit()
                s.exit()

            if ev.type == p.KEYDOWN:
                ch = ev.unicode
                if ch.isalnum():
                    t_wd += ch

                if ev.key == p.K_RETURN:
                    if t_wd == t_w:
                        u_i()
                        r = False

                if ev.key == p.K_BACKSPACE:
                    t_wd = t_wd[:-1]

                if ev.key == p.K_ESCAPE:
                    t_wd = ""

            if ev.type == p.MOUSEMOTION:
                idle = False
                idle_time = 0

        t.sleep(0.1)

    p.quit()

if __name__ == "__main__":
    i_p = 'l.png'
    u_w = '282480'
    d_i_w_f_i(i_p, u_w)
