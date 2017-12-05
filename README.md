# my_crawler
it is my final_preject XD

I want to use "requests", "opencv3" to hack in "https://portal.nctu.edu.tw/portal/login.php".

The top priority is to analysis the .jpg of "captcha".

The code:

1.get the captcha (it has four different type ,and include four digits)

2.analysis the captcha by opencv to find border

3.limit the border to select which I want to keep, and split that into pieces

4.save each one piece by format([randomint+id].jpg)(randomint in case of same file_name)
  

Issue:

1.I need use ML module like tensorflow, pytorch... to train by data(.jpg we keep)

2.here, captcha has four different type.I try each type, but the get was different from the image I watch on browser
(even I use header to pretend that I am a browser)
    
The REF:

https://www.youtube.com/watch?v=kYSxf1V-VV4
