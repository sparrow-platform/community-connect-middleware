## INTRODUCTION

- <b>Sparrow Middleware - The backbone of Sparrow platform</b><br>
Sparrow Middleware enables users to join and contribute to the Sparrow ecosystem. The users can use existing popular chat apps like WhatsApp, Facebook Messenger, SMS etc or our very own Sparrow App. The Middleware serves as a middleman for all your requests, queries and connections. With our flexible architecture developers are allowed to create their very own apps and integrate with Sparrow. This can make Sparrow similar to Assistants like Alexa without users having to install a new app for it.

- <b>What does middelware do?</b><br>
The middleware is Sparrow's interfac to various chat platforms like WhatsApp, Messenger etc. It also is the 'messaging routing engine'. It listens to the messages sent to Sparrow. The requests made are routed to the correct app and the response is served to the user. It also helps users to connect to other users like doctors and community members by routing messages between them. In this way, the middleware not only lets you talk to different apps but also fellow users.

- <b>How does it help disaster victims?</b><br>
The Sparrow platform is designed to be your assistant to help overcome a disaster. Be it pre, during or post. The Sparrow-Middleware along with the Sparrow-AI and Sparrow-Net helps with medical assistance and mental well being. Victims without worrying about installing a new app can use the existing apps to join the network. The network can provide medical assistance or connect you to medical professionals from all over the world. During disasters when the communication becomes difficult, due to our integration of offline Mesh networks the victims can get connected to Sparrow. Sparrow

- <b>Why is Sparrow different from Alexa or Google Now</b><br>
Sparrow was made with the thought of disaster management and a target of ubiquitous communication. Unlike other assistants, sparrow is ALWAYS there for you - Anywhere, Anytime, Anyhow, On any devices. Unlike other ecosystems, Sparrow is also a communications platform that reaches every person in this world. 

## OVERALL ARCHITECTURE

- Overall tech diagram 

- <b>IBM Cloud at heart</b><br>
Sparrow is driven by IBM cloud and IBM Watson. Sparrow middleware follows a microservice architechitecture residing on IBM cloud formation. The communications on Sparrow are driven by IBM Watson Assistant and IBM Watson NLP components. 

## REACHING SPARROW PLATFORM

- Non-tech description of a multi-platform aspect
  - What users need to do to reach sparrow

  Unlike other existing services, you do not need to compulsorily install our app to gain the benefits. We have made attempts to make communication ubiquitous and platform independent. You can get connected as easily as you can chat with your friends. Users can use any popularly supported chatting app to join our network. Just message our bot on the platform and you have reached sparrow. This helps users to contribute or be connected to Sparrow even while doing their own work. Alternatively, we do have our very own app with features helping to reach Sparrow in difficult situations like No internet or even no mobile network.

-
  - What all platforms are covered now, what all can be easily added, etc

  Currently, we support chat apps like WhatsApp, Facebook Messenger, SMS. With our flexible architecture adding a new platform isn&#39;t a huge task. We can easily integrate any platform which is open for developers to send and receive messages. Such platforms can be Slack, WeChat, etc

- Technical overview:
  - Architecture diagram (whatsapp etc to twilio to middleware)

 ![](data:image/*;base64,)

-
  - Messaging aggregators (Twilio/IBM botkit) - What does it do, how to add new messaging support

  The messages received from different platforms are redirected to our Webhook in our specified format. The Message aggregators make this easy by listening to all the messages received on various platforms and redirect them to our webhook. There are various commercial platforms serving this like Twilio, UIB&#39;s Unification Engine. Such platforms help to add support for various platforms easily and quickly.

  Adding new messaging support can be done by configuring the app on Twilio. Twilio supports various Channels to integrate new platforms. Just configuring them and adding the Webhook will do our work. Moreover Twilio provides SDK with a simple generalized method to send messages back to users.

-
  - Custom MQTT aspect

  Apart from Webhooks Sparrow can do messaging using MQTT protocol. This opens us to offline networks, mesh networks, IoT platforms, Project Owl, etc.

ROUTING TO EXPERTS

- Non-tech description (What does this component do?)
  - How experts register, what all is captured during registration, etc

  Sparrow allows experts all over the world to participate and join the network. Experts at any point can register themselves as expert medical professionals or even community members. Just message Sparrow that you want to register and the chatbot will enrol you with its friendly chat. Once the expert has made the request we validate the information provided and add the expert badge.

-
  - How experts and users are connected

  The user in need for expert attention can just send a message to sparrow saying to connect to expert. Once a user asks for connecting to a expert the Sparrow checks with the user requirements and assigns an expert to it. Sparrow creates a link between the user and the expert. This is done by routing the messages from user to expert and expert to users through the sparrow channel. An expert can serve only a single user at a time. This ensures providing users with the special attention that they need.

-
  - How conversations start, end, etc

  On a successful connection, both the user and the expert are notified. From then messages from both parties are routed to the other party. To disconnect either party can message sparrow to disconnect by messaging &quot;@sparrow disconnect&quot;. While being connected to another user, one can talk to sparrow by using @sparrow. All such messages are routed to the sparrow engine.

- Technical overview
  - How are connections established

  Once the request of user to connect is received, sparrow tries to find an idle expert matching the requirements of the user from the pool of experts maintained in our database. The assignment of the expert is one to one so users can get special attention. Our databases maintain what connections are active and the messages are routed to the respective users after referring to this. The connection is established by updating this database with proper receiving parties

-
  - How are experts pool maintained

  Upon verifying the information provided for registration we add them to the pool of experts. If the expert is assigned to a user it is marked as busy or else considered as idle. Other information like the field of expertise, the experience is maintained in the database. When a connection request arrives the experts from this pool are assigned after matching the required criteria

-
  - How are sessions/connections maintained

  We maintain the connection state of every user and experts. If the user/expert is connected the database points to the user/expert to whom it is connected. These entries are updated upon every new connection and cleared on disconnection. This connection state helps to route messages to the correct receiver.

ROUTING TO APPS

- Non-tech description (What does this component do?)
  - What are apps
  - How will they help users
  - How can users reach apps
  - What do apps do
- Technical overview
  - How are users connected to apps
  - How are sessions maintained
- How can developers add apps to Sparrow
  - How to add new apps
  - How are apps triggered
  - How users can interact with apps (Just ask questions, sparrow finds right app to answer the questions)
