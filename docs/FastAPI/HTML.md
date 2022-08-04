from fastapi.templating import Jinja2Templates


----------------HTML
HTML所在文件夹
template = Jinja2Templates('pages')

def 名称(request: Request):
    return template.TemplateResponse('index.html', {"request": request, 'user': {'a':'A1', 'b': 'B1'}})

HTML 内用{{名称.名称}} 访问




