API is live at https://sparrow-community-connect-middleware-noisy-bandicoot.mybluemix.net
<br><br>
## INTRODUCTION

- <b>Sparrow Middleware - The backbone of Sparrow platform</b><br>
Sparrow Middleware enables users to join and contribute to the Sparrow ecosystem. The users can use existing popular chat apps like WhatsApp, Facebook Messenger, SMS etc or our very own Sparrow App. The Middleware serves as a middleman for all your requests, queries and connections. With our flexible architecture developers are allowed to create their very own apps and integrate with Sparrow. This can make Sparrow similar to Assistants like Alexa without users having to install a new app for it.

- <b>What does middelware do?</b><br>
The middleware is Sparrow's interfac to various chat platforms like WhatsApp, Messenger etc. It also is the 'messaging routing engine'. It listens to the messages sent to Sparrow. The requests made are routed to the correct app and the response is served to the user. It also helps users to connect to other users like doctors and community members by routing messages between them. In this way, the middleware not only lets you talk to different apps but also fellow users.

- <b>How does it help disaster victims?</b><br>
The Sparrow platform is designed to be your assistant to help overcome a disaster. Be it pre, during or post. The Sparrow-Middleware along with the Sparrow-AI and Sparrow-Net helps with medical assistance and mental well being. Victims without worrying about installing a new app can use the existing apps to join the network. The network can provide medical assistance or connect you to medical professionals from all over the world. During disasters when the communication becomes difficult, due to our integration of offline Mesh networks the victims can get connected to Sparrow. Sparrow

- <b>Why is Sparrow different from Alexa or Google Now</b><br>
Sparrow was made with the thought of disaster management and a target of ubiquitous communication. Unlike other assistants, sparrow is ALWAYS there for you - Anywhere, Anytime, Anyhow, On any devices. Unlike other ecosystems, Sparrow is also a communications platform that reaches every person in this world. 


## REACHING SPARROW PLATFORM

- <b>What users need to do to reach sparrow?</b>  
Unlike other existing disaster recovery/response apps or systems, you do not need to compulsorily install our app to gain the benefits. We have made Sparrow platform completely ubiquitous and platform-independent. You can get connected as easily as you can chat with your friends. Users can use any popularly supported chatting app to join our network. Just message our bot on the platform and you have reached sparrow. This helps users to contribute or be connected to Sparrow even while doing their own work. Alternatively, we do have our very own app with features helping to reach Sparrow in difficult situations like No internet or even no mobile network.

- <b>Can I try Sparrow Platform now?</b>
Currently, we support following chat apps - WhatsApp, Facebook Messenger, SMS. We are working on making sparrow available on other Chat apps. Sparrow is coming to WeChat, Slack, Viber, Telegram by November 2019. The delayed deployment for other platforms is mainly to enable media transfer on Sparrow platform. Sparrow platform is dynamic - Onboarding a new chat platform is super simple! Reach out to us if you want Sparrow to be accessible through any platform not mentioned in our 'coming soon' list.


## OVERALL ARCHITECTURE

<p align="center">
<img max-height=500  src="https://raw.githubusercontent.com/sparrow-platform/design/master/flow%20diagrams/flow1.jpg"/>
</p>

- <b>IBM Cloud at heart</b> </br>
Sparrow is driven by IBM cloud and IBM Watson. Sparrow middleware follows a Python Flask based microservice architechitecture residing on IBM cloud formation. The communications on Sparrow are driven by IBM Watson Assistant and IBM Watson NLP components. 

- <b>Messaging Interfaces</b></br>
Sparrow middleware is currently based on combination of Twilio (https://www.twilio.com/), chat app webhooks and MQTT for getting messages various chat platforms. We plan to phase out Twilio and move to Unification engine (https://unificationengine.com/) by v0.2 release of Sparrow Platform. Twilio / Chat app webhooks point to Sparrow middleware APIs to handles messages. The messages originate from chat apps reach twilio / webhook interfaces, and are then forwarded to Sparrow APIs. Similarly messages from mesh networks / Sparrow App reach Sparrow Middleware through MQTT.

<p align="center">
<img max-height=500  src="https://raw.githubusercontent.com/sparrow-platform/design/master/flow%20diagrams/twilio_messaging.jpg"/>
</p>



- <b>Handling messages</b></br>
A. Handling at Middleware layer</br>
Sparrow middleware featurs implementation involves 2 stages. The Middleware itself intercepts the incoming messges to deliver certain communication related features. These features are essentially the ones triggered by '@sparrow' commands in messages. </br></br>
B. Handling through IBM watson assistant</br>
The Applet ecosystem and Sparrow features like SparrowAI are driven by IBM watson assistant. The fundamental idea behind all Sparrow Applets is that these Applets will essentially trigger dialogues in Watson Assistant. We are creating Sparrow App development portal as an interface to Sparrow's IBM Watson assistant. Here is a link to our Watson assistant related codes repository - https://github.com/sparrow-platform/watson-cloud-functions

<p align="center">
<img max-height=500  src="https://github.com/sparrow-platform/design/blob/master/flow%20diagrams/chatbot.jpg?raw=true"/>
</p>

- <b>Routing replies back to users</b><br>
Sparrow middleware sends back replies through the sames interfaces as message consumption interfaces. 

- <b>Stateful behaviour</b><br>
Sparrow APIs themselves are stateless - the only input they need is userIDs and messages. Session and stateful behaivour is achieved by interfacing the API with Database. We use IBM Cloudant for managing all state and session variables. 

- <b>Integrate Sparrow in your messaging app</b>
Want to create an app and make Sparrow a part of it? Sparrow platoform clients are essentially MQTT clients that allow you to create Chat interfaces interacting with Sparrow  backend.

## ROUTING TO EXPERTS

- <b>Experts registration</b><br>
Sparrow allows experts all over the world to participate and join the network. Experts at any point can register themselves as expert medical professionals or even community members. Just message Sparrow that you want to register and the chatbot will enrol you with its friendly chat. Once the expert has made the request we validate the information provided and add the expert badge.

- <b>How experts and users are connected</b><br>
The user in need for expert attention can just send a message to sparrow saying to connect to expert. Once a user asks for connecting to a expert the Sparrow checks with the user requirements and assigns an expert to it. Sparrow creates a link between the user and the expert. This is done by routing the messages from user to expert and expert to users through the sparrow channel. An expert can serve only a single user at a time. This ensures providing users with the special attention that they need.

<p align="center">
<img max-height=500  src="https://raw.githubusercontent.com/sparrow-platform/design/master/flow%20diagrams/connecting_to_expert.jpg"/>
</p>

- <b>Conversations with Experts</b><br>
On a successful connection, both the user and the expert are notified. From then messages from both parties are routed to the other party. To disconnect either party can message sparrow to disconnect by messaging '@sparrow disconnect'. While being connected to another user, one can talk to sparrow by using @sparrow. All such messages are routed to the sparrow engine.

- <b>Experts Pool</b><br>
Once the request of user to connect is received, sparrow tries to find an idle expert matching the requirements of the user from the pool of experts maintained in our database. The assignment of the expert is one to one so users can get special attention. Our databases maintain what connections are active and the messages are routed to the respective users after referring to this. The connection is established by updating this database with proper receiving parties

- <b>Ading Experts to Pool</b><br>
Upon verifying the information provided for registration we add them to the pool of experts. If the expert is assigned to a user it is marked as busy or else considered as idle. Other information like the field of expertise, the experience is maintained in the database. When a connection request arrives the experts from this pool are assigned after matching the required criteria

- <b>How are sessions/connections maintained</b><br>
We maintain the connection state of every user and experts. If the user/expert is connected the database points to the user/expert to whom it is connected. These entries are updated upon every new connection and cleared on disconnection. This connection state helps to route messages to the correct receiver.

<p align="center">
<img max-height=500  src="https://github.com/sparrow-platform/design/blob/master/flow%20diagrams/db.jpg"/>
</p>


## App ecosystem
- <b>IBM Watson at heart</b><br>
Sparrow Applet ecosystem is essentially a wrapper/interface built over Sparrow's Watson Assistant. Sparrow can deliver apps through 2 mechanisms - 
<br><br>
<b>A. Adding new dialog to Sparrow's Watson assistant</b><br>
This is extremely easy - IBM Watson Dialogue is triggered when certain question is asked. Every dialog will represent one App - Sparrow AI and Sparrow Net are such applicatins on Sparrow platform.
<br><br>
<b>B. Redirecting Sparrow to new Watson Assistant instance (Application's Watson assistant instance)</b><br>
This is what we call the 'Sparrow Ecosystem'. Sparrow middleware maintains a 'receiver' variable for every user. Default receive is SPARROW_IBM_WATSON. The middleware detects this value and the redirects every message to the corresponding IBM Watson assistant (By checking watson endpoint from database). We can easily add many more such receiver variables in the key-value map. For example, a receiver can be AMERICAN_RED_CROSS that redirects all user communication to american red cross Sparrow Applet. Due to nature of sessions on Sparrow platform, adding and navigating between different applets will be super easy. To change the app user is interacting with, all the users need to do is trigger '@sparrow' commands to change the applet they interact with! 

<p align="center">
<img max-height=500  src="https://raw.githubusercontent.com/sparrow-platform/community-connect-middleware/master/middlewareArchitecture.png"/>
</p>

## API Structure
- /middleware/receive
```
Message entry point for Sparrow platform 

Request parameters:
"From" - Sparrow UserID for messenger sender
"Body" - Message content
```

- /middleware/connect_expert
```
Connects user to a expert

Request parameters:
"sessionID" - Sparrow SessionID for the user
"type" - Type of expert to connect with
```

- /middleware/send_message
```
Sends message to some user

Request parameters:
"userID" - Sparrow userID for the receiver
"message" - Message content
```

- /visual_recognition/text
```
Returns content from media

Request parameters:
"image_url" - URL to media to extract content from
```

- /nlp/sentiment
```
Returns sentiment of text

Request parameters:
"text" - Text to extract sentiment from
```

- /nlp/entities
```
Extracts entities from text

Request parameters:
"text" - Text to extract entities from
```
