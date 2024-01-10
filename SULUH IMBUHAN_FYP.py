import tkinter as tk
import re
import time

def show_page1():
    page2_frame.pack_forget()
    page3_frame.pack_forget()
    page1_frame.pack()
    
def show_page2():
    page1_frame.pack_forget()
    page3_frame.pack_forget()
    page2_frame.pack()
    
def show_page3():
    page1_frame.pack_forget()
    page2_frame.pack_forget()
    page3_frame.pack()
    
def show_page2_from_page3():
    page3_frame.pack_forget()
    page2_frame.pack()

file_path = "C:\\Users\\Admin\\OneDrive\\Documents\\kata nama.txt" 
file_path2 = "C:\\Users\\Admin\\OneDrive\\Documents\\kata kerja.txt" 
file_path3 = "C:\\Users\\Admin\\OneDrive\\Documents\\kata_an_kan.txt" 
file_path4 = "C:\\Users\\Admin\\OneDrive\\Documents\\kekecualian.txt" 
file_path5 = "C:\\Users\\Admin\\OneDrive\\Documents\\akhiran_i.txt" 
file_path6 = "C:\\Users\\Admin\\OneDrive\\Documents\\pe.txt"
file_path7 = "C:\\Users\\Admin\\OneDrive\\Documents\\awalan_me.txt"
file_path8 = "C:\\Users\\Admin\\OneDrive\\Documents\\awalan_ber.txt"
file_path9 = "C:\\Users\\Admin\\OneDrive\\Documents\\awalan_ter.txt"
file_path10 = "C:\\Users\\Admin\\OneDrive\\Documents\\di.txt"
file_path11 = "C:\\Users\\Admin\\OneDrive\\Documents\\ke.txt"

with open(file_path, 'r') as file:
    kata_nama_list = file.read().splitlines()
with open(file_path2, 'r') as file:
    kata_kerja_list = file.read().splitlines()
with open(file_path3, 'r') as file:
    an_kan_list = file.read().splitlines()
with open(file_path4, 'r') as file:
    kekecualian_list = file.read().splitlines()
with open(file_path5, 'r') as file:
    akhiran_i_list = file.read().splitlines()
with open(file_path6, 'r') as file:
    awal_pe_list = file.read().splitlines()
with open(file_path7, 'r') as file:
    awal_me_list = file.read().splitlines()
with open(file_path8, 'r') as file:
    awal_ber_list = file.read().splitlines()
with open(file_path9, 'r') as file:
    awal_ter_list = file.read().splitlines()
with open(file_path10, 'r') as file:
    awal_di_list = file.read().splitlines()
with open(file_path11, 'r') as file:
    awal_ke_list = file.read().splitlines()
  
# Function for getting Input from textbox and updating the label with results
def updateLabel():
    inp = inputtxt.get(1.0, "end-1c")
    
    # Remove any existing tags
    inputtxt.tag_delete("error_tag")
    

    # Tokenize the input into words
    words = inp.split()

    for word in words:
        # Remove non-alphabet characters from the word
        word = re.sub(r'[^a-zA-Z]', '', word)
 
        if word.lower().startswith('pem') and word.lower().endswith('i') and word[3] not in 'aeiouy' and not word[3:] in akhiran_i_list:
            if word[3] in 'pbfv' and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pem...i')
            else:
                highlight_word(word,"red_tag")
                
                
        elif word.lower().startswith('pen') and word.lower().endswith('i') and word[3] not in 'g' and word[3] not in 'aeiouy' and not word[3:] in akhiran_i_list:
            if word[3] in 'dcjzts'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pen...i')
            else:
                highlight_word(word,"red_tag")
                               
        elif word.lower().startswith('peng') and word.lower().endswith('i') and word[3:] in akhiran_i_list :
            if word[4] in 'ghaeiouk'and len(word[4:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan peng...i')
            else:
                highlight_word(word,"red_tag")           
                
        elif word.lower().startswith('penge') and word.lower().endswith('i'):
            if len(word[5:])==3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan penge...i')
            else:
                highlight_word(word,"red_tag")
                            
        elif word.lower().startswith('per') and word.lower().endswith('i') and word[-1] not in awal_pe_list:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan per...i')                         


        elif word.lower().startswith('pe') and  word.lower().endswith('i') and not word[2:] in akhiran_i_list and word not in akhiran_i_list and not word[3:] in akhiran_i_list:
            if word[2] in 'mnnrlwpr' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pe...i')                         
            else:
                highlight_word(word,"red_tag")   

        
        elif word.lower().startswith('mem') and word.lower().endswith('i') and word[3] not in 'aeiouy'and word[3:] not in akhiran_i_list:
            if word[3] in 'pbfv'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan mem...i')    
            else:
                highlight_word(word,"red_tag")              
                
        elif word.lower().startswith('men') and word.lower().endswith('i') and word[3] not in 'aeiouyg' and word[3:] not in akhiran_i_list:
            if word[3] in 'dcjsz'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan men...i')  
            else:
                highlight_word(word,"red_tag")
                                
        elif word.lower().startswith('meng') and word.lower().endswith('i') and word[4:] not in akhiran_i_list :
            if word[4] in 'ghaeiou'and len(word[4:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan meng...i')  
            else:
                highlight_word(word,"red_tag")
                
                
        elif word.lower().startswith('menge') and word.lower().endswith('i') and word[5:] not in akhiran_i_list :
            if len(word[5:]) == 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan menge...i')
            else:
                highlight_word(word,"red_tag")

                 
        elif word.lower().startswith('me') and word.lower().endswith('i') and word[3:] not in akhiran_i_list and word[2:] not in akhiran_i_list and word not in akhiran_i_list  and word not in awal_me_list:
            if word[2] in 'mnnrlwpr' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan me..i')    
            else:
                highlight_word(word,"red_tag")

                
                 
        elif word.lower().startswith('pem') and not word.lower().endswith('an') and word not in awal_pe_list:
            if word[3] in 'bfvp' and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan pem')
            else:
                highlight_word(word,"red_tag")
                
                
        elif word.lower().startswith('pen') and not word.lower().endswith('an') and word[3] not in 'g' and word not in awal_pe_list and word[3] not in 'aeiouy':
            if word[3] in 'dcjzts'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan pen')
            else:
                highlight_word(word,"red_tag")
                               
        elif word.lower().startswith('peng') and not word.lower().endswith('an') and word not in awal_pe_list :
            if word[4] in 'ghaeiouk'and len(word[4:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan peng')
            else:
                highlight_word(word,"red_tag")           
                
        elif word.lower().startswith('penge') and not word.lower().endswith('an') and word not in awal_pe_list:
            if len(word[5:])==3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan penge')
            else:
                highlight_word(word,"red_tag")
         
        elif word.lower().startswith('per') and not word.lower().endswith('an')  and word not in awal_pe_list:
                display_highlighted_words(word,'Imbuhan awalan per')           

        elif word.lower().startswith('pe') and not word.lower().endswith('an')  and word not in awal_pe_list:
            if word[2] in 'mnnrlwprks' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan pe')                         
            else:
                highlight_word(word,"red_tag")  
              

        elif word.lower().startswith('pem') and word.lower().endswith('an')and word[3] not in 'aeiouy':
            if word[3] in 'bfvp' and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pem...an')
            else:
                highlight_word(word,"red_tag")
                
                
        elif word.lower().startswith('pen') and word.lower().endswith('an') and word[3] not in 'g' and word[3] not in 'aeiouy':
            if word[3] in 'dcjzts'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pen...an')
            else:
                highlight_word(word,"red_tag")
                               
        elif word.lower().startswith('peng') and word.lower().endswith('an') and word[:-2] not in awal_pe_list and word[4:] not in kekecualian_list and word !='penglibatan':
            if word[4] in 'ghaeiouk'and len(word[4:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan peng...an')
            else:
                highlight_word(word,"red_tag")     
                   
        elif word.lower().startswith('penge') and word.lower().endswith('an') and word[:-2] not in awal_pe_list and word[5:] not in kekecualian_list:
            if len(word[5:])==3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan penge...an')
            else:
                highlight_word(word,"red_tag")
                          
        elif word.lower().startswith('per') and word.lower().endswith('an') and word[:-2] not in awal_pe_list and word[2:] not in kekecualian_list:
                display_highlighted_words(word,'Imbuhan apitan per...an')                         
   
        elif word.lower().startswith('pe') and word.lower().endswith('an') and word[:-2] not in awal_pe_list and word[2:] not in kekecualian_list:
            if word[2] in 'mnnrlwprks' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan pe...an')                         
            else:
                highlight_word(word,"red_tag")     
                                 
                    
        elif word.lower().startswith('ber') and len(word[3:]) > 3 and word.lower().endswith('an') and word[-3]!='k' and word[:-2] not in awal_ber_list and word[3:] not in kekecualian_list:
            if word[3] not in 'r':
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan ber...an')    
            else:
                highlight_word(word,"red_tag")    
                
        elif word.lower().startswith('ke') and len(word[2:]) > 3 and word.lower().endswith('an') and word[:-2] not in awal_ke_list and word[2:] not in kekecualian_list:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan ke...an')    

        
        elif word.lower().startswith('mem') and not word.lower().endswith('kan') and word not in awal_me_list and word[3] not in 'aeiouy':
            if word[3] in 'bfvp'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan mem')    
            else:
                highlight_word(word,"red_tag")              
                
        elif word.lower().startswith('men') and not word.lower().endswith('kan') and word[3] not in 'g' and word not in awal_me_list and word[3] not in 'aeiouy' :
            if word[3] in 'dcjzys'and len(word[3:]) > 3 or word == 'menternak':
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan men')  
            else:
                highlight_word(word,"red_tag")
                                
        elif word.lower().startswith('meng') and not word.lower().endswith('kan') and word not in awal_me_list :
            if word[4] in 'ghaeiou'and len(word[4:]) > 2:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan meng')  
            else:
                highlight_word(word,"red_tag")
                
                          
        elif word.lower().startswith('me') and not word.lower().endswith('kan') and word not in awal_me_list and word !='Melayu' and word!='mega':
            if word[2] in 'mnnrlwpr' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan me')    
            else:
                highlight_word(word,"red_tag")
                                                          
        elif word.lower().startswith('menge') and not word.lower().endswith('kan') and word not in awal_me_list :
            if len(word[5:]) == 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan menge')
            else:
                highlight_word(word,"red_tag")

      
        elif word.lower().startswith('mem') and word.lower().endswith('kan') and word[3] not in 'aeiouy':
            if word[3] in 'bfvp'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan mem...kan')    
            else:
                highlight_word(word,"red_tag")              
                
        elif word.lower().startswith('men') and word.lower().endswith('kan') and word[3] not in 'g' and word[3] not in 'aeiouy':
            if word[3] in 'dcjzsy'and len(word[3:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan men...kan')  
            else:
                highlight_word(word,"red_tag")
                                
        elif word.lower().startswith('meng') and word.lower().endswith('kan'):
            if word[4] in 'ghaeiou'and len(word[4:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan meng...kan')  
            else:
                highlight_word(word,"red_tag")
                
        elif word.lower().startswith('me') and word.lower().endswith('kan'):
            if word[2] in 'mnnrlwpr' and len(word[2:]) > 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan me..kan')    
            else:
                highlight_word(word,"red_tag")
                                 
        elif word.lower().startswith('menge') and word.lower().endswith('kan'):
            if len(word[5:]) == 3:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan menge...kan')
            else:
                highlight_word(word,"red_tag")

        elif word.lower().startswith('ber') and len(word[3:]) > 3 and word.lower().endswith('kan') and word[:-3] not in awal_ber_list and word[3:] not in kekecualian_list:
            if word[3] not in 'r':
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan ber...kan')    
            else:
                highlight_word(word,"red_tag")         
                
        elif word.lower().startswith('di') and len(word[2:]) > 3 and word.lower().endswith('kan') and word[:-3] not in awal_di_list and word[2:] not in kekecualian_list:
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan apitan di...kan')
                  
        elif word.lower().startswith('ber') and len(word[3:]) > 3 and not word.lower().endswith('an') and word not in awal_ber_list:
            if word[3] not in 'r'and word != 'berkerja':
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan ber')    
            else:
                highlight_word(word,"red_tag")
                            
        elif word.lower().startswith('ter') and len(word[3:]) > 3 and word not in awal_ter_list:
            if word[3] not in 'r':
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan ter')    
            else:
                highlight_word(word,"red_tag")
        
        elif word.lower().startswith('di') and len(word[2:]) > 3 and not word.lower().endswith('kan') and word not in awal_di_list :
                highlight_word(word,"blue_tag")
                display_highlighted_words(word,'Imbuhan awalan di')
 
                 
        elif word.lower().endswith('an') and word not in kekecualian_list and word[-1] in kata_kerja_list or kata_nama_list =='k' and word[-3]!='k':
                highlight_word(word, "blue_tag")
                display_highlighted_words(word,'Imbuhan akhiran ...an') 
                      
        
        elif word.lower().endswith('kan') and word not in kekecualian_list  :
                highlight_word(word, "blue_tag")
                display_highlighted_words(word,'Imbuhan akhiran ...kan')

        elif word.lower().endswith('i') and word not in akhiran_i_list:
            highlight_word(word, "blue_tag")
            display_highlighted_words(word,'Imbuhan akhiran ...i')    
            


        else:
            pass
        

def display_highlighted_words(word,display_text):
        highlighted_listbox.insert(tk.END, f"{word} - {display_text}")
        

def highlight_word(word, tag):
    start = inputtxt.search(word, "1.0", stopindex="end", nocase=1, count=1)
    if start:
        end = f"{start}+{len(word)}c"
        inputtxt.tag_add(tag, start, end)
        if tag == "blue_tag":
            inputtxt.tag_config("blue_tag", foreground="blue")
        elif tag == "red_tag":
            inputtxt.tag_config("red_tag", foreground="red")
            
def clear_input():
    inputtxt.delete(1.0, tk.END)  # Clears the input text box
    highlighted_listbox.delete(0, tk.END)  # Clears the highlighted list box


# Top-level window

# Create the main window
root = tk.Tk()
root.title("APLIKASI MEMERIKSA IMBUHAN")


page1_frame = tk.Frame(root, width=2500, height=2000, bg='#98AFC7')
page2_frame = tk.Frame(root, bg='#98AFC7')
page3_frame = tk.Frame(root, bg='#98AFC7')


page1_label = tk.Label(page1_frame, text="SELAMAT DATANG ", font=("Helvetica", 20), fg="white", bg='#98AFC7')
page1_description = tk.Label(page1_frame, text="MARI PERIKSA PENGGUNAAN IMBUHAN ANDA!", font=("Optima", 14),
                             fg="white", bg='#98AFC7')
page1_button = tk.Button(page1_frame, text="HALAMAN 2", command=lambda: [show_page2(), animate_button()],
                         padx=20, pady=10, font=("Helvetica", 12), bg="orange", fg="white")

page1_label.pack(pady=20)
page1_description.pack(pady=10)
page1_button.pack(pady=20)

def animate_button():
    pass


page3_label = tk.Label(page3_frame, text="MASUKKAN TEKS:", font=("Helvetica", 16), fg="white", bg='#737CA1')
inputtxt = tk.Text(page3_frame, height=15, width=80, font=("Helvetica", 12))
check_button = tk.Button(page3_frame, text="PERIKSA", command=updateLabel, font=("Helvetica", 12), bg="orange", fg="white")
clear_button = tk.Button(page3_frame, text="PADAMKAN", command=clear_input, font=("Helvetica", 12), bg="red", fg="white")
highlighted_listbox = tk.Listbox(page3_frame, height=10, width=80, font=("Helvetica", 12))
back_button = tk.Button(page3_frame, text="KEMBALI", command=show_page2_from_page3, font=("Helvetica", 12), bg="green", fg="white")


page3_label.pack(pady=20)
inputtxt.pack(pady=10)
button_frame = tk.Frame(page3_frame, bg='purple')
check_button.pack(pady=10)
clear_button.pack(pady=10)
highlighted_listbox.pack(pady=10)
back_button.pack(pady=10)
button_frame.pack(pady=10)

label_box = tk.Frame(page2_frame, bg='#737CA1', padx=10, pady=10)
label_box.pack()

page2_label = tk.Label(label_box, text="Maklumat Perisian", font=("Helvetica", 20), fg="white", bg='#737CA1')
page2_label.pack()
info_text = """
Perisian ini akan membantu anda untuk memeriksa penggunaan imbuhan dalam teks. 
Sila masukkan teks di halaman tiga dan tekan pada butang 'PERIKSA' untuk mengetahuai pengunaan imbuhan dalam teks anda.
Jika perkataan diwarnakan biru bermaksud perkataan itu merupakan kata terbitan yang betul 
manakala jika perkataan diwarnakan merah bermaksud perkataan tersebut mempunyai penggunaan imbuhan yang salah
Imbuhan yang diperiksa adalah imbuhan awala, imbuhan apitan dan imbuhan akhiran.
Imbuhan yang dapat dikesan oleh perisian ini adalah imbuhan awalan meN..., imbuhan awalan peN..., imbuhan awalan ber...,
imbuhan awalan ter..., imbuhan awalan di..., imbuhan awalan ke...,
imbuhan apitan meN...kan, imbuhan apitan peN..an, imbuhan apitan di..kan,imbuhan apitan ber... kan, 
imbuhan apitan ke...kan, imbuhan apitan ke...an, imbuhan akhiran ...an, imbuhan akhiran ...kan, imbuhan akhiran ...i

"""

info_text_widget = tk.Text(page2_frame, font=("Arial", 14), bg="#123456", fg="white", wrap="word", height=10, borderwidth=2, relief="groove")
info_text_widget.insert("1.0", info_text)  # Insert your info text
info_text_widget.config(state="disabled")  # Make the widget read-only
info_text_widget.tag_configure("left", justify="left")  # Left align text
info_text_widget.tag_add("left", "1.0", "end")


page2_button = tk.Button(page2_frame, text="Periksa Imbuhan", command=lambda: [show_page3()], padx=20, pady=10,
                         font=("Helvetica", 12), bg="orange", fg="white")


page2_label.pack(pady=20)
info_text_widget.pack(pady=(10, 20), padx=20)  
page2_button.pack(pady=20)

def on_enter(e):
    page2_button.config(background="darkorange", fg="white")

def on_leave(e):
    page2_button.config(background="orange", fg="white")

page2_button.bind("<Enter>", on_enter)
page2_button.bind("<Leave>", on_leave)

show_page1()

# Start the application
root.mainloop()

