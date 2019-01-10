import wx 
import wx.html2
import shelve


myhomepage = "http://www.duckduckgo.com"
class MyBrowser(wx.Frame): 
  def __init__(self, *args, **kwds): 
    wx.Frame.__init__(self, *args, **kwds)
    self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
    self.InitUI()
    
 
  def InitUI(self):
    vsizer = wx.BoxSizer(wx.VERTICAL)
    hsizer = wx.BoxSizer(wx.HORIZONTAL)
    self.browser = wx.html2.WebView.New(self)
    vsizer.Add(self.browser, 1, wx.EXPAND, 10)
    hsizer.Add(self.browser, 1, wx.EXPAND, 10)
    self.SetSizer(vsizer)
    self.SetSizer(hsizer)
    self.ShowFullScreen(True)
    self.SetTitle('FCSD')
    self.Bind(wx.EVT_CHAR_HOOK, self.OnKeyDown)

  def showKeys(self):#user doesn't know the key bindings
    self.keys = wx.MessageBox( 'Down key: Home \n Up key: GOTO \n Left key: Back \n Right key: Forward \n Escape: Exit \n F2: Set Home Page', 'Key Bindings', wx.OK)
    self.keys.Show()
    self.keys.Destroy()
  def getURL(self): #get url to go to
    self.dlg = wx.TextEntryDialog(self, 'Enter URL', 'GOTO')
    self.dlg.SetValue('')
    if self.dlg.ShowModal() == wx.ID_OK:
      window.browser.LoadURL(self.dlg.GetValue())
    self.dlg.Destroy()
  def OnKeyDown(self, event):
    keycode = event.GetKeyCode()
    print keycode
    #ESC: 312, quit
    #LKEY: 314, back
    #RKEY: 316, fwd
    #UKEY: 317, GOTO
    #DKEY: 315, HOME
    #F1: 340, Show Keys
    if keycode == 27:
      self.Close()
    elif keycode == 314:
      try:
        self.webBack()
      except:
        print "There was a problem."
    elif keycode == 316:
      try:
        self.webFwd()
      except:
        print "There was a problem."
    elif keycode == 315:
      self.getURL()
    elif keycode == 317:
      self.homePage()
    elif keycode == 340:
      self.showKeys()
    elif keycode == 341:
      self.setHome()
    else:
      
      event.Skip()

  def webBack(event):
    window.browser.GoBack()
  def webFwd(event):
    window.browser.GoForward()
  def setHome(self):
    self.dlg = wx.TextEntryDialog(self, 'Enter your home page', 'Set Home')
    self.dlg.SetValue('')
    if self.dlg.ShowModal() == wx.ID_OK:
       d = shelve.open("homepage.db")
       d['home'] = self.dlg.GetValue()
       d.close()
    self.dlg.Destroy()
  def homePage(event):
    d = shelve.open("homepage.db")
    myhomepage = d['home']
    d.close()
    window.browser.LoadURL(myhomepage)
    
if __name__ == '__main__': 
  app = wx.App() 
  window = MyBrowser(None, -1)
  d = shelve.open("homepage.db")
  myhomepage = d['home']
  d.close()
  window.browser.LoadURL(myhomepage)  #home page, configurable eventually
  window.Show() 
  app.MainLoop() 
