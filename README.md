# Face the Facts

**Face the Facts** is aim to combine voice/face/text recognition and privacy preserved ML to support diagnosis and treatment of people with depressions. The purpose is to support a higher level of automation in either self-diagnosis of clinical identification of depression levels, which improves self-awareness of mental health and allows accurate depression detection at an early stage. Meanwhile, our proposed smart watch enhances treatment of depresssion in a more consistent manner.

According to [NHS](https://www.nhs.uk/mental-health/conditions/clinical-depression/symptoms/), depression can be detected through physical-, psychological-, and social-symptons. Psychological symptoms are commonly known, containing symptons like feeling hopeless and helpless, or having thoughts of harming oneself. Physical symptoms include examples like changes in appetite or weight, or changes of sleeping habits. Social symptoms are seen in less social activities than usual. However, existing diagnosis of depression relies on subjective answers to mental health questionnaires, which is based on the patients' memory of the past weeks or months. Even if a patient is diagnosed and gets access to depression care, consistent and customised treatment is challenging to provide. 

Here, we propose a smart watch, **Face the Facts**, with an attempt to tackle these challenges in depression detection and treatment. 

## System Design
<p align="center">
<img src="https://github.com/Yuni0217/Face_the_Facts/blob/main/others/FacetheFacts.png" alt="System" width="550px">
</p>

**Step 1 - Data Collection: ** 
We collect mainly four types of data, namely facial data collected through webcams, speech data collected through microphone, text communication data extracted from socialisation APP, as well as medical data collected through sensors or health APP. 

**Step 2 - Privacy-Preserved Machine-Learning Training/Testing: ** 
We maintain four tracks of federated learning processes, for which the collected data are applied differetial privacy policies and anonymised for training and testing. Note that historical data is trained in offline mode. Newly recorded data is trained in online mode. 

**Step 3 - Fuzzy-Logic Based Computing: ** 
The categorisation results from the previous step is fetched and delivered into a fuzzy-logic based computing process. Combined with depression membership defined by psychologists, we generate a depression score of the user. 

## Potential Attacks and Remediations

**IoT-based attacks** may appear in the smart watch and result in DoS (Denial of Services). Possible mitigation examples are OS (operating system) hardening and adoption of secure firmware update mechanisms.  

**Attacks on communication protocols** may be exploited, such as eavesdropping and replaying attacks. Possible mitigation example is applying secure key exchange protocols.

**Attacks in medical record system** may be exploited to extract or modify patients' data. Possible mitigation example is following advanced encryption standard.

**Attacks against ML training/testing system** may be triggered, such as stealthy attack. Possible mitigation example is employing encrypted transfer learning approach.

## Data
* Facial data: get through webcam embedded in our smart watch, and generates facial emotion features (to diagnose psychological symptoms).
* Speech data: get through microphone embedded in our smart watch, and generates voice emotion features (to diagnose psychological and social symptoms).
* Text communication data: get through connected socialisation APP in a phone/pad/PC, and generates textual emotion features (to diagnose psychological and social symptoms). 
* Medical data: get through sensors embedded in our smart watch and/or connected APP, and generates biomedical fectures (to diagnose physical symptoms).

## Note
The code examples in each directory, e.g. facialEmotions and textEmotions, are not our original contributions. Instead, they are fetched from open-source projects under MIT license. We added these code examples just to demonstrate the technical feasibility of our proposed smart watch depression-diagnosis system, for this "R. U. Hackathon?" activity only. We plan to work out with our own code in the future. 

## Potential Options for Mental Health Repositories
* [CMU-MOSEI](https://github.com/A2Zadeh/CMU-MultimodalSDK) for voice emotion detection.
* [Toronto emotional speech set (TESS)](https://tspace.library.utoronto.ca/handle/1807/24487) for voice emotion detection.

## Reference
Stellios, I., Kotzanikolaou, P., Psarakis, M., Alcaraz, C., & Lopez, J. (2018). A survey of iot-enabled cyberattacks: Assessing attack paths to critical infrastructures and services. IEEE Communications Surveys & Tutorials, 20(4), 3453-3495.

Mosenia, A., & Jha, N. K. (2016). A comprehensive study of security of internet-of-things. IEEE Transactions on emerging topics in computing, 5(4), 586-602.

