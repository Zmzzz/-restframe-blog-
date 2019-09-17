
from django.shortcuts import HttpResponse
def get_valid_img(request):
    import PIL
    import random
    # 随机颜色
    def random_valid_img_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    from PIL import Image,ImageDraw,ImageFont
    image=Image.new('RGB',(250,40),random_valid_img_color())
    draw=ImageDraw.Draw(image)
    font=ImageFont.truetype('static/font/kumo.ttf',28)
    valid_code=''
    for i in range(5):
         random_int=str(random.randint(0,9))
         random_upper_Eng=chr(random.randint(65,90))
         random_low_Eng=chr(random.randint(97,122))
         choice=random.choice([random_int,random_low_Eng,random_upper_Eng])
         valid_code=valid_code+choice
         draw.text([i*48,0],choice,random_valid_img_color(),font=font)
    print('系统随机生成的输入的验证码', valid_code)
    request.session['valid_code']=valid_code
    width=240
    high=80
    for i in range(10):
        x1=random.randint(0,width)
        y1=random.randint(0,high)
        x2 = random.randint(0, width)
        y2 = random.randint(0, high)
        draw.line([x1,y1,x2,y2],fill=random_valid_img_color())
    from io import BytesIO
    f=BytesIO()
    image.save(f,'png')
    data=f.getvalue()
    f.close()
    return HttpResponse(data)