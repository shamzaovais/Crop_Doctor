# Crop Doctor 🌾🩺
**Intelligent Disease Diagnosis of Crops**

Crop Doctor is a smart, accessible, and freely available mobile solution designed to identify plant diseases in real-time. By leveraging deep learning and cloud computing, it helps farmers and agronomists detect diseases early, preventing major crop yield losses.

## 🚀 Key Features
- **Intelligent Diagnostics:** Upload or capture an image of a leaf to instantly detect crop diseases.
- **Bilingual Interface:** Supports both English and Urdu for wide accessibility among regional farming communities.
- **Cloud-Powered Processing:** Heavy ML processing is offloaded to AWS, allowing the app to run smoothly on low-end devices.
- **Feedback System:** Built-in survey for farmers to submit location, farm size, and app experience to help improve the system.

## 🛠️ Technology Stack
- **Mobile Application:** Android (Requires Android 4.4+)
- **Backend Bridge Server:** Django (Deployed on Heroku)
- **Cloud Infrastructure:** Amazon Web Services (AWS)
  - **Amazon S3:** Image storage (Bucket: `agritech12`)
  - **Amazon SageMaker:** Model training, hosting, and endpoint deployment
- **Machine Learning / AI:** Convolutional Neural Networks (CNNs)

## 📊 Dataset & Model Performance
The models were trained on a dataset of 4,000 regional and natural plant images, categorized into 5 classes: Northern Leaf Blight (NLB), Grey Leaf Spot (GLS), Common Rust (CR), Healthy, and Extra Class (Outliers).

Several architectures were evaluated. The **SageMaker Built-in Model** was chosen for production due to its exceptional accuracy.

| Model Architecture | Peak Accuracy | Best Data Split |
| :--- | :--- | :--- |
| **SageMaker Built-in** | **99.95%** | 80-20 |
| **ResNet50** | 97.68% | 80-20 |
| **Keras Sequential (Custom)**| 97.05% | 80-20 |
| **AlexNet** | 96.92% | 60-40 |
| **VGG19** | 96.85% | 60-40 |

## 🏗️ System Architecture Workflow
1. **User Input:** The user captures a crop leaf image via the Android app.
2. **Cloud Storage:** The image is securely uploaded to an AWS S3 bucket.
3. **Backend Routing:** The Django Heroku server detects the upload and triggers the AWS SageMaker endpoint.
4. **Inference:** The SageMaker model analyzes the image and returns a prediction (Disease Name + Confidence %).
5. **Result Display:** The Django server sends this data back to the mobile app, displaying it to the user.

## 👥 Team & Credits
Developed at the **Nisar Aziz Agritech Center** (Namal Institute Mianwali).
- **Developers:** Umair Nawaz, Syed Ahmed
- **Supervisors:** Dr. Malik Jahan Khan, Dr. Fareed Zaffar

---
*Empowering farmers with AI to protect crops and ensure better harvests.*

<img width="1661" height="3030" alt="image_original (3)" src="https://github.com/user-attachments/assets/a3e91e10-5e60-476a-8d25-6db228139ec3" />
<img width="3264" height="2448" alt="image_original (4)" src="https://github.com/user-attachments/assets/afd595d9-5402-4ab3-9786-0d4a704a6a42" />
<img width="1661" height="3030" alt="image_original" src="https://github.com/user-attachments/assets/1e391e68-c681-4727-b748-409dec4b2bc4" />
<img width="1643" height="3030" alt="img 1-1" src="https://github.com/user-attachments/assets/6ca3b55f-6d6e-4f85-b0db-c3f749dfef46" />
<img width="720" height="1520" alt="img_5" src="https://github.com/user-attachments/assets/d591903b-9522-44bd-b23d-3e5f3668d0c1" />
<img width="3264" height="3030" alt="img_6" src="https://github.com/user-attachments/assets/1beb79c2-cc2f-44c6-972e-159ed1d87548" />



