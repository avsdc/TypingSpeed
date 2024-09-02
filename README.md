
 Typing Speed And Accuracy

Description:

Typing Speed And Accuracy is an application in Python and Tkinter. Variables counter, var1, var2,
user_txt_wordcount, accurate_wds, are initialized to 0, variables elapsed_secs, start_time, current_time 
are initialized to 0.0, ctime is initialized to True, and user_str is initialized to “ “.

A new window and configuration is created. A number of frames are added using the Frame class, and 
a number of labels are added using the Label class.

When the program is run, the user interface that appears, displays the original_text created using Text 
class placed on the first frame, that inserts the original_text_para chosen randomly from a list of three paragraphs.
The original_text_para is split by “ “, and the length of the resulting list, called original_text_wordcount is 
determined using the len function. 

The user_text is also created in a similar manner, and the string “Start typing here.” is inserted. The get function 
retrieves the string inserted into the user_text, and places in the user_text_para. The length of the user_text_para 
gives the user_text_wordcount.

When the user is ready, he/she should click the START button. This triggers the start() function that sets focus to the 
user_text. The user should clear the text in the user_text, and start typing text, using the original_text as a guide. 
The start function also sets start_time to time.time. Then the function start_timer() is called.  The variable elapsed_secs 
is incremented by one, and timer_label is updated using config(). As long as variable ctime declared on top is 'True', the 
timer_label gets updated with the elapsed_secs. The timer_label uses the after function, that takes as input 1000ms, and a 
recursive call to start_timer(). Thus, the timer_label gets updated every second, and gets displayed.

When the user completes typing in the original_text_para, he/she should click on the STOP button. This triggers the 
stop_timer() function. The user_str is retrieved from the user_text area using get. The len function applied to user_str 
returns the wordcount in the user_text area. 

The calculate_typing_speed() function is called. The typing speed is calculated by dividing user_text_wordcount by 
elapsed_secs/60. The type_speed_label is then updated to this value, var1, and var1 is returned from the function

The calc_accuracy function is then called. The original_text_para is split by spaces to create the original_list,
and user_str is split by spaces to create the user_list. The number of correct words is obtained by anding the 
set(original_list) and set(user_list), which finds the words from user_list that are common to words in the 
original_list. The length of correct_words gives number of accurate_wds. Accuracy is determined by dividing 
accurate_wds by original_text_wordcount and multiplying by 100, and rounding to 2 places, into var2 that is 
returned from the function.

In the function stop_timer(), var1 is a return value from function calculate_typing_speed(), and var2 is a 
return value from calc_accuracy() function. The labels type_speed_label and accuracy_label, are then updated 
to var1 and var2 respectively using config.

The reset_all() function resets user_text to the string “Start typing here.”, the timer_label, type_speed_label,
 and accuracy_label are reset to 0.0.


Usage:

The project was created in Python 3.12 and Tkinter, and Pycharm Community edition.

