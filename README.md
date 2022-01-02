# large format laser cutter
A laser cutter designed for cutting fabric. Because it is so large, it can hide under your rug when not in use.

Right now the files are all in OnShape, a free cloud based CAD program. You can edit and download all the files here:
https://cad.onshape.com/documents/a2abef0dbf10d935f35e9834/w/c5f3a70774121f6ae469bc75/e/f884df53f987339406035ad5

I will be documenting this more when I can. If you want to contribute, we could use a directory of the STL files in a pull request.

Here is a video of the first full range of motion test.
https://twitter.com/TLAlexander/status/1477460542713327616

Since it is designed to cut fabrics for sewing, there is also a camera for scanning in existing patterns. Code TBD
https://twitter.com/TLAlexander/status/1476853052640411650

Some detail photos are here:
https://twitter.com/TLAlexander/status/1475784906672263171

This design is 100% open source. I do not need anything in return for this work. Please take it and use it in whatever way benefits you. You are invited to fork the design and make it your own, sell kits if you want, anything. The work is licensed CC0 - public domain. If all engineers do this with their work, we can change the world.

Stepper motors used: SL Motor PN: CF3925-100-SL
I disassembled an old 3D printer for them but I noticed there are some here. Any steppers of the same size would be fine. Or adust the design for the sise you have:
https://www.ebay.com/itm/313684051490

Uses eight 623zz bearings.
The current design uses M3 screws to hold those bearings in, with the M3 screws just screwed in to plastic, not really ideal.

Gantry is a 1" aluminum square tube from Home Depot.
Carriage uses 16 6801 bearings.

You could also probably use Openbuilds V-slot linear rail and the associated gantry. Note it is 20mm not 1" so you would need to change the clamp or design a clamp sleeve.
https://openbuildspartstore.com/v-slot-20x20-linear-rail/
https://openbuildspartstore.com/v-slot-gantry-kit-20mm/

I ordered the "40W Pro" (7.5 watt optical power) solid state cutting laser from here:
https://www.aliexpress.com/item/1005001708213195.html

Which should be similar to the one featured in this review:
https://www.youtube.com/watch?v=QrtGMzzSWDo

You will need some control board. I used one from another old 3D printer and flashed a fresh copy of Marlin firmware on to it.
https://github.com/MarlinFirmware/Marlin

See this video for instructions on how to configure. I will post my configs here soon.
https://www.youtube.com/watch?v=J9vxJT5Tgh4
