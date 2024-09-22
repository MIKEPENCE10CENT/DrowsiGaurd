# DrowsiGuard

## Abstract
**DrowsiGuard** is a real-time monitoring system designed to assess driver alertness using facial landmark detection, with the goal of enhancing road safety. The system analyzes key facial features captured via a camera to track drowsiness indicators and compute a fatigue score. When this score falls below a predefined threshold, an alert is triggered to remind the driver to rest. By leveraging advanced facial recognition technology, the system provides accurate and timely warnings to reduce accidents caused by driver fatigue.

## Explanation of the Idea
Driver fatigue is a leading cause of road accidents, contributing to around **100,000 crashes annually** over the past two years. Fatigue diminishes reaction times and focus, significantly increasing accident risk. To address this critical issue, **DrowsiGuard** utilizes advanced facial landmark detection technology to continuously monitor drivers in real-time.

The system calculates a **fatigue score** based on several indicators, including:
- Eye closure
- Yawning frequency
- Blinking patterns
- Head tilt
- Duration of continuous driving

When the fatigue score falls below a predefined threshold, the system generates an alert, recommending the driver take a break. This multi-parameter approach offers a reliable solution to improving road safety by providing timely warnings and helping to reduce drowsiness-related accidents.

---

## Block Diagram

### 1. Facial Landmark Detection
The system leverages **facial landmarks** for real-time analysis. Specific facial features are assigned numbers for easy reference, focusing primarily on the **eyes**, **mouth**, and **head position**.

![Picture10](https://github.com/user-attachments/assets/5fa6ca22-62fa-407d-974a-bb33a7fff221)

![Picture11](https://github.com/user-attachments/assets/b30f3bb3-5a18-4790-9af3-d167fcc4a8ae)

### 2. Eye Aspect Ratio (EAR)
The **Eye Aspect Ratio (EAR)** is used to measure the openness of the driver’s eyes. The system continuously calculates the EAR, and when it drops below a defined threshold, it indicates that the driver’s eyes are closed, triggering an alert.

![Picture7](https://github.com/user-attachments/assets/500d4e9e-dff7-4ca6-aaa0-237c5feafb9a) ![Picture8](https://github.com/user-attachments/assets/319ec7ba-feae-4ce7-b941-543a05258c37) ![Picture9](https://github.com/user-attachments/assets/9e6561ae-3b15-4d35-82cc-31745b2101a3)


### 3. Yawning Frequency (Mouth Aspect Ratio - MAR)
The **Mouth Aspect Ratio (MAR)** is calculated to detect yawning by measuring the vertical and horizontal distances of the mouth. The frequency of yawns is used as another metric to assess fatigue. Frequent yawning can signal driver drowsiness.

 ![Picture4](https://github.com/user-attachments/assets/8291f3e1-0308-4df8-b745-9f3320a697d7) ![Picture5](https://github.com/user-attachments/assets/155fe2a6-4cdd-444e-bf3a-900bc0d6b6b1) ![Picture6](https://github.com/user-attachments/assets/16927678-5f27-4a1a-8ed7-e45d8984de5b)




### 4. Eye Blinking Frequency
**Blinking frequency** is tracked using the **EAR** metric. Abnormal blinking patterns, such as excessive or infrequent blinking, may indicate drowsiness and lower the overall fatigue score. The system monitors these patterns in real-time to assess the driver’s condition.

![Picture3](https://github.com/user-attachments/assets/d3c191be-3f38-405c-bc80-9ce214913b75)


### 5. Head Tilt Detection
The **tilt of the head** is continuously measured to detect signs of fatigue or inattention. By calculating the angle between the line joining the two eyes and the horizontal axis, the system detects if the driver’s head is tilted. Persistent head tilt can indicate fatigue or drowsiness.

  
![Picture2](https://github.com/user-attachments/assets/deaff30a-2823-428d-848f-13c98ac85445) ![Picture1](https://github.com/user-attachments/assets/cc6c8161-227c-4506-8560-f0946f1c7fc7)



### 6. Travel Time Monitoring
**DrowsiGuard** tracks the vehicle’s running time to periodically remind the driver to take breaks after extended periods. A **GPS module** is connected via a serial interface to the SK-AM62A-LP, which processes location data to calculate travel time and distance. Based on these calculations, the system periodically issues reminders for the driver to take rest breaks.


---

## System Components

### Hardware
- **Camera**: Captures real-time video of the driver's face.
- **SK-AM62A-LP**: Microcontroller used for processing data from the camera and GPS module.
- **GPS Module**: Used to calculate travel time and provide periodic rest reminders.
  
### Software
- **OpenCV**: Library for facial landmark detection and real-time image processing.
- **Dlib**: For facial landmark extraction.
- **Python**: Primary programming language for data processing.
  
---

## Working Process

1. The system captures real-time video of the driver’s face using a camera.
2. **Facial landmarks** are detected and tracked in real-time using **Dlib** and **OpenCV**.
3. Key parameters such as **Eye Aspect Ratio (EAR)**, **Mouth Aspect Ratio (MAR)**, and **Head Tilt** are continuously monitored.
4. A **fatigue score** is computed by analyzing eye closure, yawning, blinking, head tilt, and driving duration.
5. If the fatigue score falls below the threshold, the system triggers an alert, warning the driver to take a break.
6. The system also periodically reminds the driver to rest based on the travel time.

---

## Future Scope
- **Advanced Machine Learning Models**: Integrate machine learning algorithms to improve the accuracy of drowsiness detection.
- **Vehicle Integration**: Direct integration with the vehicle's system to automate rest-stop reminders.
- **IoT Connectivity**: Enable cloud-based data tracking and analytics for better monitoring and record-keeping.
- **Mobile App Interface**: Develop a mobile app that can sync with the system for real-time alerts and notifications.

---

## Conclusion
**DrowsiGuard** is an innovative solution aimed at reducing road accidents caused by driver fatigue. By employing advanced facial detection techniques, the system provides real-time drowsiness detection and timely alerts, promoting safer driving conditions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
