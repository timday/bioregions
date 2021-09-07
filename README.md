bioregions
==========

Python code to identify which One Earth Bioregion (if any) contains a given longitude-latitude coordinate.

Dependences
-----------
Requires `geojson`: pip-installable <https://pypi.org/project/geojson/>

`Bioregions2020.geojson` data originates with One Earth <https://www.oneearth.org/bioregions/> and is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/).

Examples
--------
Usage examples in:

* `./test-pts.py` identifies the Bioregions of some longitude-latitude coordinates in the code.  (Takes a few seconds to load the bioregion data before it outputs anything).
* `./test-map-txt.py` tests points on a longitude-latitude array (takes a few 10s of seconds to run).
* `./test-map-plot.txt` similar to the above but plots a finer grid graphically (matplotlib dependency).  Takes significantly longer to run.

The `./test-map-txt.py` output is:

```
Loading Bioregions2020.geojson...
   This work is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/).
..loaded 185 bioregions
     -180-170-160-150-140-130-120-110-100-090-080-070-060-050-040-030-020-010+000+010+020+030+040+050+060+070+080+090+100+110+120+130+140+150+160+170
 85:                                 NA2 NA2 NA2 NA2 NA2                                         PA1 PA1                                             
 80:                     NA2 NA2 NA2 NA2 NA2 NA2 NA2 NA1 NA1 NA1 NA1 NA1     PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA1         PA4 PA4     
 75:                     NA2 NA2 NA2 NA2 NA2 NA2         NA1 NA1 NA1 NA1         PA1 PA1 PA1 PA1 PA1 PA1 PA1 PA4 PA4 PA4 PA4 PA4 PA4 PA4 PA4 PA4     
 70: PA5 PA5 NA3 NA3 NA3 NA2 NA2 NA2 NA2 NA2 NA2 NA2     NA1 NA1 NA1     PA1 PA1 PA3 PA3 PA3 PA4 PA4 PA4 PA4 PA4 PA4 PA4 PA4 PA7 PA7 PA7 PA7 PA4 PA5 
 65: PA5 NA4 NA4 NA4 NA6 NA6 NA7 NA2 NA2 NA2 NA2 NA2 NA2 NA1 NA1     PA2 PA2     PA3 PA8 PA8 PA8 PA8 PA4 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA5 
 60: PA5 NA4 NA4 NA5 NA5 NA6 NA7 NA9 NA9 NA2 NA2 NA2 NA2             PA2 PA9 PA9 PA8 PA11PA8 PA8 PA8 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA7 PA6 PA5 
 55: NA4 NA4 NA4 NA4 NA5 NA15NA8 NA8 NA9 NA9 NA9 NA9 NA9                 PA9 PA9 PA10PA12PA11PA11PA12PA7 PA34PA34PA35PA7 PA7 PA7 PA7 PA6 PA6 PA6 PA6 
 50: NA4 NA4             NA15NA14NA12NA12NA9 NA9 NA9 NA9 NA9             PA9 PA10PA12PA12PA12PA16PA16PA34PA32PA32PA36PA44PA7 PA44PA46PA6 PA6 PA6 NA4 
 45:                         NA17NA13NA12NA11NA11NA10NA10NA9             PA10PA10PA13PA14PA16PA16PA33PA32PA32PA31PA38PA43PA43PA44PA46PA47PA6         
 40:                         NA18NA19NA20NA21NA24NA25            PA21    PA20PA20PA19PA19PA18PA17PA33PA32PA31PA39PA39PA43PA42PA46PA46PA47            
 35:                         NA31NA19NA20NA25NA24                    PA22PA23PA23PA23PA18PA18PA26PA27PA29PA41PA40PA40PA40PA49PA49PA47PA47            
 30: OC11                    NA30NA29NA20NA25NA25                    PA24PA23PA24PA24PA24PA24PA26PA29PA29PA30IM5 PA40PA40PA52PA50IM14OC10            
 25:     OC11OC11                NT28NA29NT27NT26                    PA24PA25PA25PA24PA24PA24PA26PA26PA29IM4 IM6 IM6 PA52IM13IM13IM14OC10            
 20:     OC11OC11                NT29NT28NT27NT26NT26NT26            PA24PA25PA25PA25PA25PA25PA26PA26PA26IM4 IM8 IM6 IM12IM13IM15                OC7 
 15:     OC11                        NT28NT25NT25NT23NT26            AT24AT20AT23AT23AT23AT23AT22AT22    IM1 IM8 IM9 IM12IM12IM15                OC7 
 10:                             NT29        NT24NT23NT21                AT19AT20AT20AT23AT23AT22AT22    IM1 IM8 IM9 IM9 IM12IM15    OC8 OC8 OC7 OC7 
  5:         OC4                         NT24NT24NT22NT21NT16            AT19AT19AT16AT16AT16AT21AT22    IM1 IM2     IM18IM16IM15OC8 OC8 OC8 OC8 OC7 
  0:     OC5 OC4                         NT9 NT10NT19NT20NT16NT15NT14            AT17AT14AT12AT21        IM1         IM18IM16AU14AU13AU13AU13    OC7 
 -5: OC5 OC5         OC2                     NT11NT18NT17NT17NT15NT14            AT13AT13AT11AT7 AT5     IM1         IM18IM16AU14AU14AU13AU13AU12    
-10: OC5 OC5 OC4 OC4 OC2                     NT8 NT18NT17NT13NT15                AT11AT11AT11AT7 AT5 AT4                 IM17AU15AU8 AU13AU13AU12AU11
-15: OC6 OC5     OC3 OC3                         NT5 NT12NT13NT14                AT10AT11AT11AT7 AT6 AT4                     AU8 AU8 AU8 AU10AU12AU11
-20: OC6 OC6 OC3 OC3 OC3                         NT8 NT4 NT14NT14NT14            AT10AT9 AT11AT6 AT6 AT4                     AU8 AU7 AU8 AU9 AU10AU11
-25:             OC3 OC3 OC3     OC1         NT7 NT8 NT4 NT13NT14                    AT9 AT8 AT6 AT6                     AU6 AU7 AU7 AU7 AU9 AU10AU10
-30: AU1                         OC1             NT5 NT4 NT14                        AT9 AT8                                 AU5 AU7 AU7 AU9 AU2 AU2 
-35: AU1                                     NT7 NT5 NT3 NT14            AT1         AT2 AT7                 AT3             AU5     AU4 AU3 AU2 AU1 
-40: AU1                                         NT2 NT3                 AT1                                 AT3                     AU4 AU3     AU1 
-45: AN4                                         NT2                                         AN3 AN3                                     AU3     AU1 
-50: AN4                                     NT1 NT2 NT2                                                 AN3                                     AN4 
-55:                                             NT1 NT2     AN2 AN2         AN3                         AN3                                 AN4 AN4 
-60:                                                 AN2 AN2 AN2 AN2                                                                                 
-65:                                             AN2 AN2 AN2                                 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 
-70:                     AN1     AN1 AN1 AN1 AN1 AN2 AN1             AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 
-75: AN1     AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 
-80: AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 
-85: AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 AN1 

```
