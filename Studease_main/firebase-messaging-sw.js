// Scripts for firebase and firebase messaging
importScripts('https://www.gstatic.com/firebasejs/9.6.8/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.6.8/firebase-messaging-compat.js');

// Initialize the Firebase app in the service worker by passing the generated config
var firebaseConfig = {
    apiKey: "AIzaSyA6KNM_WBmpX5Jq9FqzgVJO6KiArXifS_4",
    authDomain: "chatapp-f722f.firebaseapp.com",
    projectId: "chatapp-f722f",
    storageBucket: "chatapp-f722f.appspot.com",
    messagingSenderId: "348189912931",
    appId: "1:348189912931:web:b6aa699bb65e15a340ad56",
    measurementId: "G-M9X3G0J8NL"
};

firebase.initializeApp(firebaseConfig);

// Retrieve firebase messaging
const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log(payload)
    console.log("Received background message", payload);
    const { title, link_url, ...options } = payload.data;
    // Customize notification here
    self.registration.showNotification(title, {...options });
});

self.addEventListener("notificationclick", (event) => {
    console.log("Click:", event);
    event.notification.close();

    event.waitUntil(clients.matchAll({ type: "window" }).then((clientList) => {
        console.log("what is client list", clientList);
        for (const client of clientList) {
            if (client.url === "/" && "focus" in client) return client.focus();
        }
        if (clients.openWindow && Boolean(event.notification.data.link_url)) return clients.openWindow(event.notification.data.link_url);
    }).catch(err => {
        console.log("There was an error waitUntil:", err);
    }));
});