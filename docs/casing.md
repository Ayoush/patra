| Word | Rule      | Example                                        |
|------|-----------|------------------------------------------------|
| and  | lowercase | `daman and diu` -> `Daman and Diu`             |
| of   | lowercase | `festival of light` -> `Festival of Light`     |
| the  | lowercase | `he is the mayor` -> `He Is the Mayor`         |
| in   | lowercase | `he is in there` -> `He Is in There`           |
| at   | lowercase | `we are at red fort` -> `We Are at Red Fort`   |
| by   | lowercase | `shop by the river` -> `Shop by the River`     |
| ngo  | uppercase | `ngo colony` -> `NGO Colony`                   |
| co   | uppercase | `travel co` -> `Travel CO`                     |
| pvt  | uppercase | `travel pvt` -> `Travel PVT`                   |
| ltd  | uppercase | `legal ltd` -> `Legal LTD`                     |
| llp  | uppercase | `restaurant llp` -> `Restaurant LLP`           |

#`_LOWER_WORDS`
_LOWER_WORDS Contains "and", "of", "the", "in", "at", "by" : article, preposition that are used to join main words rather than being a part of it. 
Example 'daman and diu' turns into 'Daman and Diu' not 'Daman And Diu'.

#`_UPPER_WORDS`
_UPPER_WORDS Contains "ngo", "co", "pvt", "ltd", "llp" : abberivations that are common in oraginization names within their address; 
Example 'travel co' turns into 'Travel CO'.

#`Example`
Example: `ngo colony` → `NGO Colony`


# Know Limitation

Ordinals (4th, 1st) are a known limitation. They have no dedicated rule and goes regular capitlization (.capitalize()) since digits can't be capitalized 
so '4th' stays '4th' and '4TH' turns '4th'. 
