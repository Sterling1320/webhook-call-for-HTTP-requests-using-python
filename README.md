# webhook-call-for-HTTP-requests-using-python
I was working on creating a whatsapp/telegram based chatbot for my college, because i felt the college website lacked the appeal and aesthetics and also it was full of bugs. I had always found whatsapp chatbots as really cool and i thought to myself, "Why not create one for my college". So began my journey to create a better experience for my fellow college mates. However i had no idea how to proceed with the project, what was involved in creating a chatbot or how to deploy it. I mean there were so many options to choose from, twillio, dialogflow, watson or the good old fashioned python scratch model. In the end, i realised that the scratch method was too tedious as we had reviews each week and i couldnt balance my academics and this project all together. So I opted to use Dialogflow to create my Agent (or the bot). The UI of dialogflow was fairly easy to use and feature rich. I defined the whole conversation flow on dialogflow by defining intents and different entities that would handle the user inputs. 

I planned to implement the following things via my chabot

1. College Information
2. Admission process
3. Academic calendar
4. Faculty Information
5. Admission and fees Portal
6. Campus Map
7. Club information
8. Fill exam form/ Check Result
9. College Library 
10. Hostel Admission
11. Fees Structure
12. College social media handles
13. Meet my elder brother (surprise)
14. Other College Facilities

most of the things above could be handled using the intents, entities and the responses but other things like Faculty Information, College library, Clubs and Fees Status (I did not include fees status in my final list of functionalities but for the sake of this example im including it) required connectivity to databases. ALso deploying the whole agent on whatsapp would require a subscription to the whatsapp business API (which my stingy college refused to pay for). The professors asked me to create a working prototype which successfully handled user queries and only then they would consider paying for the API fees. So the problem was that i had created sample databases on my local mysql command line client on my system and i had to connect it to the dialogflow agent to retrieve whatever information was stored on the database table. 

So to connect a database on my localhost to handle HTTP requests, i had to use python and ngrok together to make it work. I used python to create a webhook code which would simply extract the parameters sent by the agent , for this to work you would first need to go to the fulfillment section in the dialogflow console and enable fulfillments, leave the fulfillment URL blank for the meantime. Next go to the specific intent that you need the database connectivity for and enable webhook fulfillment for the same. Next step is to create a flask module which would connect to the local databases and parse the HTTP requests and generate responses. Once the flask app is ready and working, run it and then open the ngrok app. Since your python app and the databases are on your local system, you need tunneling to esatblish a working connection between the dialogflow client and the localhost.

Ngrok is used for this very purpose, open ngrok and enter the command "ngrok HTTP 5000" which forwards any http requests to or from the local host to the dialogflow client. When you run that command, you get a URL which is the webhook fulfillment that you need. Copy that link to the fulfillments section (which we left blank earlier) and once you do that, a connection between your localhost and the dialogflow client has been established and you can successfully retrieve any queries from the table.

While functional, this method has a lot of problems; it is too tedious, there is a limit of 2hrs for forwarding or tunneling using ngrok free version and not to mention it is not feasible as it only works as long as you keep providing the tunneling for fulfillment so this method is helpful when you want to check or learn how to handle HTTP requests or how to connect the dialogflow to the local system. It is however, non-functional for final deployment and usage and you can only use a single database at a time and only for simple requests, the more tables you add the more tricky or complex the flask code becomes. Therefore this was only for the sake of experimentation. My final methadology to tackle all of these issues is in another repository that you can find on my profile which is functional.
