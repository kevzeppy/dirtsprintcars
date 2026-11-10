# Legends photo credits (staged, not wired in)

Staged 2026-11-10 on `grok/history-legends-photos` for the Legends page (`legends.html` / `legends-data.json`). Nothing in those two files was edited; News/Features wire the photos in later.

- Files: `images/legends/<slug>.jpg`, resized to at most 1200 px wide. The slug is the legend's exact `name` in `legends-data.json`, lowercased, with runs of non-letters/digits turned into `-` (the same rule `build_legends.py` uses for the `bio-<series-id>-<slug>` ids).
- Coverage: 38 of 40 legends have a photo. No permitted photo was found for **Frankie Kerr** and **Brent Kaeding** (candidate sources at the bottom).
- Permission basis: WRG/World of Outlaws (kit approved by Nick Graziano on 2026-10-30) and USAC (approved by Richie Murray on 2026-11-02, "properly credit the writer and / or photographer"). See `MEDIA-PERMISSIONS.md`.
- Credit line format: use the "Credit" column as the visible photo credit. Where the photographer is unknown, the credit names the outlet and says so.

## 1. Filename to legend mapping

| legends-data.json `name` | File | `bio-` id(s) on legends.html | Series sections |
|---|---|---|---|
| Steve Kinser | `images/legends/steve-kinser.jpg` | `bio-woo-steve-kinser` | World of Outlaws |
| Sammy Swindell | `images/legends/sammy-swindell.jpg` | `bio-woo-sammy-swindell` | World of Outlaws |
| Donny Schatz | `images/legends/donny-schatz.jpg` | `bio-woo-donny-schatz` | World of Outlaws |
| Mark Kinser | `images/legends/mark-kinser.jpg` | `bio-woo-mark-kinser` | World of Outlaws |
| Doug Wolfgang | `images/legends/doug-wolfgang.jpg` | `bio-woo-doug-wolfgang` | World of Outlaws |
| Rico Abreu | `images/legends/rico-abreu.jpg` | `bio-hl-rico-abreu` | High Limit Racing |
| Kyle Larson | `images/legends/kyle-larson.jpg` | `bio-hl-kyle-larson` | High Limit Racing |
| Dale Blaney | `images/legends/dale-blaney.jpg` | `bio-all-stars-dale-blaney` | All Star Circuit of Champions |
| Kenny Jacobs | `images/legends/kenny-jacobs.jpg` | `bio-all-stars-kenny-jacobs` | All Star Circuit of Champions |
| Chad Kemenah | `images/legends/chad-kemenah.jpg` | `bio-all-stars-chad-kemenah` | All Star Circuit of Champions |
| Tim Shaffer | `images/legends/tim-shaffer.jpg` | `bio-all-stars-tim-shaffer` | All Star Circuit of Champions |
| Frankie Kerr | **no photo** | `bio-all-stars-frankie-kerr` | All Star Circuit of Champions |
| Joey Saldana | `images/legends/joey-saldana.jpg` | `bio-all-stars-joey-saldana` | All Star Circuit of Champions |
| Jack Hewitt | `images/legends/jack-hewitt.jpg` | `bio-all-stars-jack-hewitt`, `bio-usac-sprint-jack-hewitt`, `bio-silver-crown-jack-hewitt` | All Star Circuit of Champions; USAC Sprint Cars; USAC Silver Crown |
| Pancho Carter | `images/legends/pancho-carter.jpg` | `bio-usac-sprint-pancho-carter`, `bio-usac-triple-crown-pancho-carter` | USAC Sprint Cars; USAC Triple Crown |
| Dave Darland | `images/legends/dave-darland.jpg` | `bio-usac-sprint-dave-darland`, `bio-usac-midget-dave-darland`, `bio-usac-triple-crown-dave-darland` | USAC Sprint Cars; USAC Midgets; USAC Triple Crown |
| Brady Bacon | `images/legends/brady-bacon.jpg` | `bio-usac-sprint-brady-bacon` | USAC Sprint Cars |
| Tom Bigelow | `images/legends/tom-bigelow.jpg` | `bio-usac-sprint-tom-bigelow` | USAC Sprint Cars |
| Tracy Hines | `images/legends/tracy-hines.jpg` | `bio-usac-sprint-tracy-hines`, `bio-usac-triple-crown-tracy-hines` | USAC Sprint Cars; USAC Triple Crown |
| Justin Grant | `images/legends/justin-grant.jpg` | `bio-usac-sprint-justin-grant` | USAC Sprint Cars |
| Brent Kaeding | **no photo** | `bio-narc-brent-kaeding` | Northern Auto Racing Club (NARC) |
| Gary Wright | `images/legends/gary-wright.jpg` | `bio-ncra-gary-wright`, `bio-ascs-gary-wright` | National Championship Racing Association (NCRA); American Sprint Car Series (ASCS) |
| Terry Gray | `images/legends/terry-gray.jpg` | `bio-ncra-terry-gray`, `bio-ascs-terry-gray`, `bio-uscs-terry-gray` | National Championship Racing Association (NCRA); American Sprint Car Series (ASCS); United Sprint Car Series (USCS) |
| Sam Hafertepe Jr. | `images/legends/sam-hafertepe-jr.jpg` | `bio-ascs-sam-hafertepe-jr` | American Sprint Car Series (ASCS) |
| Jason Johnson | `images/legends/jason-johnson.jpg` | `bio-ascs-jason-johnson` | American Sprint Car Series (ASCS) |
| Mel Kenyon | `images/legends/mel-kenyon.jpg` | `bio-usac-midget-mel-kenyon` | USAC Midgets |
| Rich Vogler | `images/legends/rich-vogler.jpg` | `bio-usac-midget-rich-vogler` | USAC Midgets |
| Bob Wente | `images/legends/bob-wente.jpg` | `bio-usac-midget-bob-wente` | USAC Midgets |
| Kody Swanson | `images/legends/kody-swanson.jpg` | `bio-silver-crown-kody-swanson` | USAC Silver Crown |
| Dave Steele | `images/legends/dave-steele.jpg` | `bio-silver-crown-dave-steele` | USAC Silver Crown |
| Tony Stewart | `images/legends/tony-stewart.jpg` | `bio-usac-triple-crown-tony-stewart` | USAC Triple Crown |
| J.J. Yeley | `images/legends/j-j-yeley.jpg` | `bio-usac-triple-crown-j-j-yeley` | USAC Triple Crown |
| Jerry Coons Jr. | `images/legends/jerry-coons-jr.jpg` | `bio-usac-triple-crown-jerry-coons-jr` | USAC Triple Crown |
| Chris Windom | `images/legends/chris-windom.jpg` | `bio-usac-triple-crown-chris-windom` | USAC Triple Crown |
| Logan Seavey | `images/legends/logan-seavey.jpg` | `bio-usac-triple-crown-logan-seavey` | USAC Triple Crown |
| Kenny Weld | `images/legends/kenny-weld.jpg` | `bio-old-school-kenny-weld` | Old School Legends |
| Jan Opperman | `images/legends/jan-opperman.jpg` | `bio-old-school-jan-opperman` | Old School Legends |
| Jac Haudenschild | `images/legends/jac-haudenschild.jpg` | `bio-old-school-jac-haudenschild` | Old School Legends |
| Bobby Allen | `images/legends/bobby-allen.jpg` | `bio-old-school-bobby-allen` | Old School Legends |
| Brad Doty | `images/legends/brad-doty.jpg` | `bio-old-school-brad-doty` | Old School Legends |

Extra file: `images/legends/jac-haudenschild-alt.jpg` is an alternate for Jac Haudenschild (see his entry below).

## 2. Photo details

| Legend | File | Source | Source URL / path | Credit | Suggested caption | How the driver was confirmed | Permission basis | Notes |
|---|---|---|---|---|---|---|---|---|
| Donny Schatz | `images/legends/donny-schatz.jpg` (1200x800) | WRG Dropbox | WRG Dropbox: /World of Outlaws Sprint Cars/Photos/2025 Photos by Trent Gower/_2025_PlatinumDrivers/Donny_Schatz/ByTrentGower_DonnySchatzCandid.jpg | Trent Gower / World of Outlaws | Donny Schatz in his Tony Stewart Racing firesuit, 2025 World of Outlaws portrait. | Dropbox folder and file name name him ("Donny_Schatz", "DonnySchatzCandid"); suit shows Tony Stewart Racing, Curb and the "15" 15th-anniversary patch. Same folder has his No. 15 car. | WRG Dropbox |  |
| Kyle Larson | `images/legends/kyle-larson.jpg` (1172x720) | WRG Dropbox | WRG Dropbox: /World of Outlaws Sprint Cars/Photos/2025 Photos by Trent Gower/0807_KnoxvilleNationals_Night 2/Kyle_Larson_Trent_Gower_Photo.jpg | Trent Gower / World of Outlaws | Kyle Larson in Casey's Victory Lane at the Knoxville Nationals, 2025. | File name names him; the winner's check in the photo is made out to "Kyle Larson"; Casey's Victory Lane and Knoxville Nationals signage visible. WoO driver page uses the same image captioned "Kyle Larson in Knoxville Raceway Victory Lane". | WRG Dropbox |  |
| Rico Abreu | `images/legends/rico-abreu.jpg` (1200x1800) | WRG Dropbox | WRG Dropbox: /World of Outlaws Sprint Cars/WoO_Drivers w:NASCAR connects/Rico Abreu/WoO_RicoAbreu_ByPaulArch.JPG | Paul Arch / World of Outlaws | Rico Abreu, World of Outlaws. | "ABREU" is lettered on the suit belt; folder and file name name him. | WRG Dropbox |  |
| Tony Stewart | `images/legends/tony-stewart.jpg` (1200x800) | WRG Dropbox | WRG Dropbox: /World of Outlaws Sprint Cars/WoO_Drivers w:NASCAR connects/Tony Stewart/WoO_TonyStewart_ByChrisOwens.jpg | Chris Owens / World of Outlaws | Tony Stewart, World of Outlaws. | Folder and file name name him; no on-image text, so identification rests on the WRG file label. | WRG Dropbox |  |
| Chris Windom | `images/legends/chris-windom.jpg` (1200x800) | WRG Dropbox | WRG Dropbox: /World of Outlaws Sprint Cars/Photos/2025 Photos by Trent Gower/_2025_PlatinumDrivers/Chris_Windom/ByTrentGower_ChrisWindom7Scar.jpg | Trent Gower / World of Outlaws | Chris Windom's NOS Energy Drink sprint car, 2025 World of Outlaws. | "WINDOM" is lettered on the top wing; folder and file name name him. | WRG Dropbox |  |
| Steve Kinser | `images/legends/steve-kinser.jpg` (1200x1500) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Steve-Kinser (gallery image "2004-08-11 Knoxville WoO Steve Kinser PAUL ARCH PHOTO img143") | Paul Arch / World of Outlaws | Steve Kinser at Knoxville Raceway, Aug. 11, 2004. | WoO gallery title/alt text names him and gives the date and track; Quaker State suit matches his No. 11 car in the same gallery. | worldofoutlaws.com |  |
| Sammy Swindell | `images/legends/sammy-swindell.jpg` (1200x1916) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Sammy-Swindell (gallery image "1997-08 Knoxville Sammy Swindell PAUL ARCH PHOTO img160 (80)") | Paul Arch / World of Outlaws | Sammy Swindell at Knoxville Raceway, August 1997. | WoO gallery title names him, Knoxville, August 1997; Channellock suit matches the Channellock No. 1 car in the sibling photo of the same session (img160 (77)). | worldofoutlaws.com |  |
| Mark Kinser | `images/legends/mark-kinser.jpg` (1200x800) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Mark-Kinser (gallery image "1999-08-13 Knoxville WoO Mark Kinser PAUL ARCH PHOTO img040") | Paul Arch / World of Outlaws | Mark Kinser's No. 5 Mopar sprint car at Knoxville Raceway, Aug. 13, 1999. | WoO gallery title names him, track and date; No. 5 Mopar car. Car photo, driver not visible. | worldofoutlaws.com |  |
| Doug Wolfgang | `images/legends/doug-wolfgang.jpg` (1200x806) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Doug-Wolfgang (gallery image "Lawrenceburg, IN WOO, Doug Wolfgang-8 EDIT") | World of Outlaws photo (photographer not identified) | Doug Wolfgang's sprint car at a World of Outlaws race in Lawrenceburg, Ind. | "WOLFGANG" is lettered on the car side; WoO gallery title names him and the location. Car photo; year unknown. | worldofoutlaws.com |  |
| Kenny Jacobs | `images/legends/kenny-jacobs.jpg` (974x702) | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2019/12/22015823/Picture4.png | Max Dolder / World of Outlaws | Kenny Jacobs' No. 71M sprint car, St. Augustine, Fla., Feb. 12, 1994. | "Driver Kenny Jacobs" is lettered on the car; WoO caption reads "2.12.94 St. Augustine, FL: Kenny Jacobs (Max Dolder photo)". Car photo. | worldofoutlaws.com |  |
| Jason Johnson | `images/legends/jason-johnson.jpg` (1072x652) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Jason-Johnson (gallery image "Wjason johnson won son vl") | World of Outlaws photo (photographer not identified) | Jason Johnson in victory lane, World of Outlaws. | WoO gallery file name/alt text names him; no on-image name text. Track, date and the child with him are not identified, so the caption stays generic. | worldofoutlaws.com | Identified only by WoO gallery label; event unknown |
| Joey Saldana | `images/legends/joey-saldana.jpg` (300x450) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Joey-Saldana (gallery image "Joey Saldana") | World of Outlaws photo (photographer not identified) | Joey Saldana, World of Outlaws. | "JOEY SALDANA" is printed on the backdrop behind him; WoO gallery label names him. Small source image (about 200x300). | worldofoutlaws.com | Low resolution source |
| Tim Shaffer | `images/legends/tim-shaffer.jpg` (1200x800) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Tim-Shaffer (gallery image "Vegas Night One - Tim Shaffer", file 022719_Shaffer2_DB3Imaging.jpg) | DB3 Imaging / World of Outlaws | Tim Shaffer's team in victory lane, Vegas night one, World of Outlaws (file dated 02/27/19). | WoO gallery alt text reads "Vegas Night One - Tim Shaffer"; this is a group victory-lane photo with a Feature Winner sign, so Shaffer is not individually pinpointed. | worldofoutlaws.com | Group photo; Shaffer not individually pinpointed |
| Chad Kemenah | `images/legends/chad-kemenah.jpg` (1200x1336) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Chad-Kemenah (gallery image "2006-02-08 Volusia All Stars Chad Kemenah ARCH PHOTO 048a") | Paul Arch / World of Outlaws | Chad Kemenah at Volusia, Feb. 8, 2006 (All Stars). | WoO gallery title names him, the date and "Volusia All Stars"; no on-image name text. | worldofoutlaws.com |  |
| Jack Hewitt | `images/legends/jack-hewitt.jpg` (1200x800) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Jack-Hewitt (gallery image "1995-04-02 Winchester USAC Sprints Jack Hewitt PAUL ARCH scan0011 (1)") | Paul Arch / World of Outlaws | Jack Hewitt in a USAC sprint car at Winchester, April 2, 1995. | WoO gallery title names him, the track, series and date; no on-image name text. Matches the USAC profile photo of Hewitt (moustache, dark curly hair). | worldofoutlaws.com |  |
| Jan Opperman | `images/legends/jan-opperman.jpg` (1200x777) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Jan-Opperman (gallery image "Jan Opperman's Bogar #90, USAC race, Eldora, OH_edited-2-8") | World of Outlaws photo (photographer not identified) | Jan Opperman's Bogar No. 90 at a USAC race at Eldora Speedway, Ohio. | WoO gallery title names him, the Bogar No. 90 and the track; No. 90 visible on the car. Year unknown. | worldofoutlaws.com | Colour-faded scan |
| Bobby Allen | `images/legends/bobby-allen.jpg` (1200x1500) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Bobby-Allen (gallery image "1987-05-24 Hagerstown WoO Bobby Allen PAUL ARCH PHOTO img403 (1)") | Paul Arch / World of Outlaws | Bobby Allen at Hagerstown, May 24, 1987, World of Outlaws. | WoO gallery title names him, the track and date; no on-image name text. | worldofoutlaws.com |  |
| Brad Doty | `images/legends/brad-doty.jpg` (1200x1500) | worldofoutlaws.com | https://worldofoutlaws.com/drivers/?driver=Brad-Doty (gallery image "2020-07-14 WoO Attica Brad Doty PAUL ARCH PHOTO DSC_5192 (530)a") | Paul Arch / World of Outlaws | Brad Doty at Attica, July 14, 2020, World of Outlaws. | WoO gallery title names him, the track and date; no on-image name text. | worldofoutlaws.com |  |
| Dale Blaney | `images/legends/dale-blaney.jpg` (1172x720) | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2025/11/13090923/Blaney.jpg | Tyler Carr / World of Outlaws | Dale Blaney in the car built by his brother Dave Blaney at Sharon Speedway, World of Outlaws. | WoO caption: "Dave Blaney's curious creation was victorious as his brother Dale drove it to a historic Sharon win with the World of Outlaws (Tyler Carr Photo)"; "BLANEY" lettered on the wing. Car photo, driver not visible. | worldofoutlaws.com |  |
| Sam Hafertepe Jr. | `images/legends/sam-hafertepe-jr.jpg` (1023x685) | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2021/03/22010445/WSam-Hafertepe-Jr..jpg | David Sink / World of Outlaws | Sam Hafertepe Jr.'s No. 15 sprint car, World of Outlaws (2021 story). | "HAFERTEPE" lettered on the car; WoO caption "A win at Devil's Bowl would be the 2nd of Hafertepe's Outlaw career. [David Sink]". Car photo. | worldofoutlaws.com |  |
| Kenny Weld | `images/legends/kenny-weld.jpg` (1200x876) | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2019/12/22015726/Screen-Shot-2019-12-25-at-7.24.55-AM.png | World of Outlaws archive photo (photographer not identified) | Kenny Weld after his fifth straight track title, Williams Grove, Pa., Oct. 5, 1974. | WoO caption: "10.5.74 Williams Grove, PA: Kenny Weld after fifth straight track title". Driver kneeling beside the No. 23 car. | worldofoutlaws.com | Archive scan; photographer unknown |
| Jac Haudenschild | `images/legends/jac-haudenschild.jpg` (586x720) | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2024/05/21234353/Sheldon_Jac.jpg | Trent Gower / World of Outlaws | Jac Haudenschild with his son Sheldon Haudenschild (cropped to Jac), World of Outlaws. | WoO alt text: "Sheldon Haudenschild stands next to his father - Jac Haudenschild"; Jac is the older man at right (cropped to him). Alternate archive image "Jac Haudenschild 1986" is staged as jac-haudenschild-alt.jpg. | worldofoutlaws.com |  |
| Brady Bacon | `images/legends/brady-bacon.jpg` (1200x675) | usacracing.com news | https://www.usacracing.com/news/circle-city-usac-sprint-car-results-july-28-2026 | Ryan Sellers / USAC | Brady Bacon in victory lane after winning round five of USAC Indiana Sprint Week at Circle City Raceway (July 28, 2026). | USAC caption: "Brady Bacon captured round five of USAC NOS Energy Drink Indiana Sprint Week ... at Circle City Raceway. (Ryan Sellers Photo)"; "BRADY BACON" is printed on the winner's check in the photo. | USAC press-release photo |  |
| Justin Grant | `images/legends/justin-grant.jpg` (1200x675) | usacracing.com news | https://www.usacracing.com/news/2025-grant-wins-usac-curb | Josh James Artwork / USAC | Justin Grant, 2025 Mike Curb USAC National Drivers Champion. | USAC caption names him; "GRANT" is lettered on the windshield header above him. | USAC press-release photo |  |
| Logan Seavey | `images/legends/logan-seavey.jpg` (1200x675) | usacracing.com news | https://www.usacracing.com/news/2024-usac-sprint-review | Josh James Artwork / USAC | Logan Seavey, 2024 USAC AMSOIL Sprint Car National Champion. | USAC caption names him; no on-image name text (identified by the USAC caption). | USAC press-release photo |  |
| Kody Swanson | `images/legends/kody-swanson.jpg` (1200x675) | usacracing.com news | https://www.usacracing.com/news/2024-usac-silver-crown-season-review | Josh James Artwork / USAC | Kody Swanson, 2024 USAC Silver Crown National Champion. | USAC caption names him; no on-image name text (identified by the USAC caption); matches the USAC driver-page headshot. | USAC press-release photo |  |
| J.J. Yeley | `images/legends/j-j-yeley.jpg` (1200x675) | usacracing.com news | https://www.usacracing.com/news/j-j-yeley-sweeps-wild-usac-cra-calistoga-return | A.J. Johnson / USAC | J.J. Yeley (in race suit, left of center) in victory lane after winning the USAC CRA race at Calistoga (Aug. 30, 2025 per the winner's check). | USAC caption "Winner J.J. Yeley. (A.J. Johnson Photo)"; the check reads Champion, Aug. 30, 2025. Group photo: Yeley is the person in the race suit, but he is not individually labeled. | USAC press-release photo | Group victory-lane photo; Yeley not individually labeled |
| Dave Darland | `images/legends/dave-darland.jpg` (1171x1781) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/dave-darland | USAC (photographer not identified) | Dave Darland, USAC. | USAC Hall of Fame page names him and "Dave DARLAND" is lettered on the suit; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Pancho Carter | `images/legends/pancho-carter.jpg` (600x893) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/pancho-carter | USAC (photographer not identified) | Pancho Carter, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Tom Bigelow | `images/legends/tom-bigelow.jpg` (600x803) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/tom-bigelow | USAC (photographer not identified) | Tom Bigelow, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Tracy Hines | `images/legends/tracy-hines.jpg` (600x400) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/tracy-hines | USAC (photographer not identified) | Tracy Hines, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Mel Kenyon | `images/legends/mel-kenyon.jpg` (600x416) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/mel-kenyon | USAC (photographer not identified) | Mel Kenyon, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Rich Vogler | `images/legends/rich-vogler.jpg` (600x848) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/rich-vogler | USAC (photographer not identified) | Rich Vogler, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Bob Wente | `images/legends/bob-wente.jpg` (600x887) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/bob-wente | USAC (photographer not identified) | Bob Wente, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Dave Steele | `images/legends/dave-steele.jpg` (600x750) | usacracing.com profile | https://www.usacracing.com/hall-of-fame-inductees/dave-steele | USAC (photographer not identified) | Dave Steele, USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Jerry Coons Jr. | `images/legends/jerry-coons-jr.jpg` (1200x800) | usacracing.com profile | https://www.usacracing.com/drivers/jerry-coons-jr | USAC (photographer not identified) | Jerry Coons Jr., USAC. | USAC profile page names him; no photographer credit on the page. | USAC site photo (profile page, not a press release) | USAC profile headshot; photographer unknown |
| Gary Wright | `images/legends/gary-wright.jpg` (400x400) | ascsracing.com (WRG) | https://ascsracing.com/drivers/?driver=Gary-Wright (image https://cdn.dirtcar.com/wp-content/uploads/sites/42/2026/05/18151339/Gary-Wright-Driver-Page-Headshots.jpg) | ASCS / World Racing Group (photographer not identified) | Gary Wright, ASCS. | ASCS driver page names him; "Gary Wright" is stitched in script on the suit. | WRG-owned ASCS site; confirm it falls under the WRG permission (the permission email names the Dropbox kit) | ASCS site photo; confirm scope of WRG permission |
| Terry Gray | `images/legends/terry-gray.jpg` (400x400) | ascsracing.com (WRG) | https://ascsracing.com/drivers/?driver=Terry-Gray (image https://cdn.dirtcar.com/wp-content/uploads/sites/42/2026/05/18124817/Terry-Gray-Driver-Page-Headshots.jpg) | ASCS / World Racing Group (photographer not identified) | Terry Gray, ASCS. | ASCS driver page names him; no on-image name text. | WRG-owned ASCS site; confirm it falls under the WRG permission (the permission email names the Dropbox kit) | ASCS site photo; confirm scope of WRG permission |
| Jac Haudenschild (alternate) | `images/legends/jac-haudenschild-alt.jpg` | worldofoutlaws.com (media library) | https://cdn.worldofoutlaws.com/wp-content/uploads/2019/03/22022848/Jac-Haudenschild-1986.jpg | World of Outlaws archive photo (photographer not identified) | Jac Haudenschild, 1986. | Identified only by the WoO media-library title "Jac Haudenschild 1986"; Nance-sponsored sprint car. | worldofoutlaws.com | Use only if the main Jac photo is rejected |

## 3. Photos to double-check before they go live

- **Jason Johnson** (`images/legends/jason-johnson.jpg`): Identified only by WoO gallery label; event unknown.
- **Joey Saldana** (`images/legends/joey-saldana.jpg`): Low resolution source.
- **Tim Shaffer** (`images/legends/tim-shaffer.jpg`): Group photo; Shaffer not individually pinpointed.
- **Jan Opperman** (`images/legends/jan-opperman.jpg`): Colour-faded scan.
- **Kenny Weld** (`images/legends/kenny-weld.jpg`): Archive scan; photographer unknown.
- **J.J. Yeley** (`images/legends/j-j-yeley.jpg`): Group victory-lane photo; Yeley not individually labeled.
- **Dave Darland** (`images/legends/dave-darland.jpg`): USAC profile headshot; photographer unknown.
- **Pancho Carter** (`images/legends/pancho-carter.jpg`): USAC profile headshot; photographer unknown.
- **Tom Bigelow** (`images/legends/tom-bigelow.jpg`): USAC profile headshot; photographer unknown.
- **Tracy Hines** (`images/legends/tracy-hines.jpg`): USAC profile headshot; photographer unknown.
- **Mel Kenyon** (`images/legends/mel-kenyon.jpg`): USAC profile headshot; photographer unknown.
- **Rich Vogler** (`images/legends/rich-vogler.jpg`): USAC profile headshot; photographer unknown.
- **Bob Wente** (`images/legends/bob-wente.jpg`): USAC profile headshot; photographer unknown.
- **Dave Steele** (`images/legends/dave-steele.jpg`): USAC profile headshot; photographer unknown.
- **Jerry Coons Jr.** (`images/legends/jerry-coons-jr.jpg`): USAC profile headshot; photographer unknown.
- **Gary Wright** (`images/legends/gary-wright.jpg`): ASCS site photo; confirm scope of WRG permission.
- **Terry Gray** (`images/legends/terry-gray.jpg`): ASCS site photo; confirm scope of WRG permission.

All USAC profile headshots (Darland, Carter, Bigelow, Hines, Kenyon, Vogler, Wente, Steele, Coons Jr.) come from usacracing.com Hall of Fame / driver pages, not from a press release, so Richie Murray's "press release photos" wording may not strictly cover them. The two ASCS headshots (Gary Wright, Terry Gray) come from ascsracing.com, a WRG site, while the WRG permission email names the Dropbox kit. A one-line confirmation from USAC / WRG would settle both. Replacement photos from USAC press releases or the WRG Dropbox can be swapped in under the same filenames.

## 4. No permitted photo found

### Frankie Kerr (`bio-all-stars-frankie-kerr`)
Searched: WRG Dropbox (all folders), worldofoutlaws.com media library and driver page, usacracing.com (2,088 news pages, driver and Hall of Fame pages), USAC press email (only the permission thread exists). Candidates to ask permission from:
- John Mahoney Photos via Bloomington Speedway / sprintsource.com: https://www.sprintsource.com/news/?i=179539
- Gene Marderness photo, PennLive (Frankie Kerr, No. 23): https://www.pennlive.com/sports/2013/06/no_23_frankie_kerr_central_pas.html
- All Star Circuit of Champions (allstarsprints.com) and the National Sprint Car Hall of Fame (sprintcarhof.com) archives
- RacersReunion (user-submitted, Craig Bontrager): http://racersreunion.com/photos/a-young-frankie-kerr-17535/

### Brent Kaeding (`bio-narc-brent-kaeding`)
Searched the same places; the only WoO item is a 1994 Peoria pack photo (cars in a pack, not usable). Candidates to ask permission from:
- National Sprint Car Hall of Fame (sprintcarhof.com), Kaeding inductee page: https://www.sprintcarhof.com/helper_pages/FileGet.aspx?id=281
- HammerDown / John's Racing Photos: https://www.hammerdownusa.com/KaedingBrent.html and https://www.hammerdownusa.com/images9.htm
- Racing Hero's (wagtimes.com): http://www.wagtimes.com/driverbrentkaeding.html
- NARC and Calistoga Speedway / Silver Dollar Speedway (Chico) photographers

## 5. Other sources checked

- WRG Dropbox: all folders listed recursively (about 2,500 files). Files are mostly numbered; only the `WoO_Drivers w:NASCAR connects` folders and the `_2025_PlatinumDrivers` / `WIX Drivers` folders name drivers. Larson, Schatz, Abreu, Stewart and Windom came from there.
- USAC: no photo-bearing press emails are in Gmail (only the permission thread). usacracing.com news pages were scanned for captions naming a legend; Bacon, Grant, Seavey, Swanson and Yeley have single-subject, captioned, credited photos. Everyone else uses the USAC Hall of Fame / driver profile photo.
