<img width="1280" height="516" alt="bottom and top base" src="https://github.com/user-attachments/assets/a72bf673-bdfa-46b3-bd8a-dae29594d746" />**Bilal’s MacroPad v2**  
It is my first ever engineering-related project and I think I did really good. It consists of 6 keys using Seeed XIAO RP2040 with a rotary encoder and custom built case.

It will be helping me making my time more efficient and help me in tasks that are very common but are taking too much time off my schedule + I can always change its code to program it the way I want.

**Features:** 

* 6 MX-style keys (in a 3×2 layout)  
* EC11 rotary encoder  
  (Rotate: Volume Up / Down  
  Press: Mute)  

* Direct GPIO wiring  
* Macro-ready firmware \- keys can be easily remapped  
* No RGB \- clean, simple, and functional (and maybe minimalistic)

**CAD Model:**  
The model is really simple, just using the simple guide. Top and bottom part held together with 4 M3 screws and headset inserts while having cut-outs for 6 switches and a rotary knob.

It has 2 separate printed parts, a bottom base that holds the pcb and everything on top while the top plate hides it all.

<img width="1280" height="516" alt="Fully assembled v3" src="https://github.com/user-attachments/assets/e2459848-3ac2-45fc-b659-d681264c884a" />

<img width="1280" height="516" alt="fully assembled 2" src="https://github.com/user-attachments/assets/f6d97bec-a7b9-4ce3-a79d-ca4f9aeddd1d" />


<img width="1280" height="516" alt="bottom and top base" src="https://github.com/user-attachments/assets/69e50b64-cd38-4f37-831e-099af4a4bae4" />

 
Made in Fusion360 (using it for the first time btw :\>).
**PCB:**  
Here is my PCB\! I made it myself in KiCad with the help of a tutorial at HackClub and some google too\! It is a 2 layered PCB board with through-hole XIAO RP2040, 6 switches and a rotary knob.
<img width="728" height="450" alt="Schematics" src="https://github.com/user-attachments/assets/af6f2f65-3031-4fcd-ac38-6c5367b3d93d" />

Schematic

<img width="520" height="543" alt="PCB Wiring" src="https://github.com/user-attachments/assets/0829bb81-7acb-4dc5-a74a-877ac90cd269" />

PCB  
**Firmware:**  
This hackpad uses KMK firmware for everything, written in CircuitPython it can handle 6 keys functions (which is really easy to change, just edit it in keyboard.keymap in [main.py](http://main.py)), a rotary knob for volume up/down and pressing it down mutes the volume.

## **Bill of Materials (BOM)**

* 1× Seeed XIAO RP2040 (through-hole)  
* 6× MX-style mechanical switches  
* 6× Blank DSA keycaps (white)  
* 1× EC11 rotary encoder  
* 4× M3×16mm screws  
* 4× M3 heatset inserts  
* 1× 3D printed case (top \+ bottom)  
* Custom PCB (2-layer)  
* CircuitPython \+ KMK firmware

## **Notes**

* No RGB LEDs were used in this design.  
* All parts comply with the provided allowed materials list (by hackclub).  
* The project stays within all size and input limits.
