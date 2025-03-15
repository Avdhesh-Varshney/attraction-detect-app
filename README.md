# 📜 AI-Powered Face Attractiveness Detector with Streamlit Interface 

<div align="center">
  <img src="https://futurefive.co.nz/uploads/story/2018/07/27/ThinkstockPhotos-872707982.webp" />
</div>

### 🎯 About the Project 

The **Face Attractiveness Detection Model** leverages deep learning to assess facial attractiveness. Built with **Streamlit**, the app allows users to upload images, videos, or use live cameras for real-time evaluation. The model uses **pretrained neural network weights** from Google Drive, downloaded via `gdown`. The **FaceAttractivenessApp module** handles core processing, while Streamlit ensures an intuitive interface. The architecture supports diverse input formats and accurate predictions.

### 📊 Dataset and Notebook 

- **Dataset:** [CelebA Dataset on Kaggle](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset)
- **Kaggle Notebook:** [Face Attraction Detection Model](https://www.kaggle.com/code/avdhesh15/face-attraction-detection-model/notebook)

### ⚙️ Tech Stack 

| Category                | Technologies                                      |
|----------------|-----------------------------------|
| **Languages**           | Python                                        |
| **Libraries/Frameworks**| TensorFlow, Keras, OpenCV, MTCNN, PIL, NumPy, gdown |
| **Cloud Storage**      | Google Drive                                  |
| **Tools**             | GitHub, Git, VS Code                          |
| **Development Environment**| Jupyter Notebook                            |
| **Deployment**         | Streamlit                                      |

### 📝 Description 

The model predicts facial attractiveness from static images, video feeds, or live camera streams via a deep learning pipeline.

### 🔍 Project Explanation 

#### 🧩 Dataset Overview & Features 

The dataset includes 40 features and 202,599 entries.

| Feature                | Description                                      | Values |
|----------------|-----------------------------------|----------------|
| 5_o_Clock_Shadow | Shadow near chin and jawline | 0 (No), 1 (Yes) |
| Arched_Eyebrows | Curved eyebrows | 0 (No), 1 (Yes) |
| Attractive | Aesthetic appeal | 0 (No), 1 (Yes) |
| Bags_Under_Eyes | Dark circles or puffiness | 0 (No), 1 (Yes) |
| Bald | No hair on scalp | 0 (No), 1 (Yes) |
| Smiling | Smile expression | 0 (No), 1 (Yes) |
| Young | Youthful appearance | 0 (No), 1 (Yes) |

(Additional features omitted for brevity)

#### 🛤 Project Workflow 

1. **Data Preprocessing:** Clean and augment the dataset.
2. **Model Training:** Train Inception V3 deep learning model.
3. **Evaluation:** Assess performance and accuracy.
4. **Model Generation:** Save as a `.keras` file.
5. **Conversion:** Convert to TensorFlow Lite format.
6. **Deployment:** Integrate with Streamlit for user interaction.

### ✅ Conclusion 

Inception V3 shows promising performance with **86.80% accuracy**.

#### 🔗 Useful Links 

- [Deployed Model](https://attraction-detect.streamlit.app/)
- [Binary Model File](https://www.kaggle.com/code/avdhesh15/face-attraction-detection-model/output)

<div align="center">
  <h3>Show some &nbsp;❤️&nbsp; by &nbsp;🌟&nbsp; this repository!</h3>
</div>

<a href="#top"><img src="https://img.shields.io/badge/-Back%20to%20Top-red?style=for-the-badge" align="right"/></a>
