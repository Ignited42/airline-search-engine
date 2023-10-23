
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD9Stcjm50EWTqkAiyr0_nY9BgpHTIEUsE",
  authDomain: "flighttoolapp.firebaseapp.com",
  databaseURL: "https://flighttoolapp-default-rtdb.firebaseio.com",
  projectId: "flighttoolapp",
  storageBucket: "flighttoolapp.appspot.com",
  messagingSenderId: "763505994866",
  appId: "1:763505994866:web:2ed9cf37e13e92e4f2a6eb",
  measurementId: "G-5LPMMFYKN1"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);