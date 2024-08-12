from flet import *
def main(page:Page):
    page.title="Mohammed"
    page.bgcolor="yellow"
    page.appbar=AppBar(
        bgcolor="red",
        title=Text("حمادي منال"),
        center_title=True,
        leading=Icon(icons.HOME),        
        actions=[
            IconButton(icons.NOTIFICATIONS),
            IconButton(icons.HOME),
        ]                      
    )
    page.vertical_alignment="center"
    page.horizontal_alignment="center"
    te=Text(value="Hammadi Mohammed",color="red")    
      
    te.size=30
    def yu(e):
        te.value=int(tef.value)*2
        page.update()
    
    tef=TextField(label="t", on_change=yu,width=300)
    page.add(tef)    
    page.add(te)
    page.update()
    
app(main)
