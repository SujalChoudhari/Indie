import IndieEngine as ie
ie.app.init()
ie.app.scalable = True
ie.app.caption = "Indie Editor"
ie.app.background_colour = ie.Colour().make(11,11,11)


#Theme Colours
light_green = ie.Colour().make(35,105,105)
dark_green = ie.Colour().make(10,20,20)
darker_green = ie.Colour().make(5,10,10)
black = ie.Colour().make(11,11,11)
highlight = ie.Colour().make(30,30,30)
light = ie.Colour().make(222,222,222)
accent = ie.Colour().make(30,30,20)

inactive = ie.Colour().make(0,0,0)
active = ie.Colour().make(20,80,80)

navbar_font  = ie.Font("Resources/font_small.ttf",15)

def editor():
    
    window_inspector = ie.Inspector([300,100],[200,300],0,2,"Inspector")
    navbar = ie.Navbar([0,0],[ie.app.screen_size[0],30],0,0,darker_green)
    dropdown_windows = ie.Dropdown([navbar.position[0],navbar.position[1]+20],[150,100],0,1,dark_green)

    btn_navbar_files = ie.Button("File",navbar_font,light_green,None)
    btn_navbar_windows = ie.Button("Windows",navbar_font,light_green,None)

    btn_dropdow_windows_inspector = ie.Button("Inspector",navbar_font,light_green,None)
    btn_dropdow_windows_hierarchy = ie.Button("Heirarchy",navbar_font,light_green,None)

    navbar.add_button(buttons=[btn_navbar_windows,btn_navbar_files])
    dropdown_windows.add_button([btn_dropdow_windows_inspector,btn_dropdow_windows_hierarchy])
    

    demo1 = "this is a text"
    demo2 = "can you read this?"
    demo3 = 12345
    demo4 = "inspector window is ready, can you rate the colour scheme?"


    def Awake():
        window_inspector.listen([demo2,"demo2"],[demo1,"demo1"],[demo3,"demo3"],[demo4,"demo4"])
        window_inspector.is_active = False


    def Update():
        if btn_dropdow_windows_inspector.ispressed: #this is continously going True
            window_inspector.is_active =True

        if btn_navbar_windows.isselected:
            dropdown_windows.isfocused = True
        
    def Draw():
        window_inspector.blit()
        navbar.blit()
        dropdown_windows.blit()


    def Inputs(event,mouse):
        demo2,demo1,demo3,demo4 = window_inspector.controls(event,mouse)
        navbar.controls(event,mouse)
        dropdown_windows.controls(event,mouse)

    ie.app.run(awake=Awake,update=Update,draw=Draw,inputs=Inputs)


editor()