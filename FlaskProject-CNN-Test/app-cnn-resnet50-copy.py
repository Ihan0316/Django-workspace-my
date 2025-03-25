# import os
# import torch
# import torchvision.transforms as transforms
# from flask import Flask, request, jsonify, render_template
# from PIL import Image
# from model import load_model, load_model2
#
# # Flask 앱 생성
# app = Flask(__name__)
# app.config["UPLOAD_FOLDER"] = "static/uploads"
#
# # CNN 모델 로드
# model = load_model()
#
# # ResNet50 모델 로드
# model2 = load_model2()
#
# # 클래스 이름
# class_names = ["Hammer", "Nipper"]
#
# # 이미지 전처리 함수
# def transform_image(image):
#     transform = transforms.Compose([
#         transforms.Resize((224, 224)),
#         transforms.ToTensor(),
#     ])
#     return transform(image).unsqueeze(0)  # 배치 차원 추가
#
# # 이미지 전처리 함수
# def transform_image2(image):
#     transform = transforms.Compose([
#         transforms.Resize((224, 224)),
#         transforms.ToTensor(),
# 		transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])
#     return transform(image).unsqueeze(0)  # 배치 차원 추가
#
#
# # 웹페이지 렌더링
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# # 이미지 업로드 및 분류 API
# @app.route("/classify", methods=["POST"])
# def classify_image():
#     if "image" not in request.files:
#         return jsonify({"error": "No image file"}), 400
#
#     image_file = request.files["image"]
#     if image_file.filename == "":
#         return jsonify({"error": "No selected file"}), 400
#
#     image = Image.open(image_file)
#     image = transform_image(image)
#
#     # 모델 예측
#     with torch.no_grad():
#         output = model(image)
#         probabilities = torch.nn.functional.softmax(output[0], dim=0)
#         predicted_idx = torch.argmax(probabilities).item()
#         confidence = probabilities[predicted_idx].item()
#
#     response_data = {
#         "class": class_names[predicted_idx],
#         "confidence": round(confidence * 100, 2),
#     }
#     return jsonify(response_data)
#
# # 이미지 업로드 및 분류 API
# @app.route("/classify2", methods=["POST"])
# def classify_image2():
#     if "image" not in request.files:
#         return jsonify({"error": "No image file"}), 400
#
#     image_file = request.files["image"]
#     if image_file.filename == "":
#         return jsonify({"error": "No selected file"}), 400
#
#     image = Image.open(image_file)
#     image = transform_image2(image)
#
#     # 모델 예측
#     with torch.no_grad():
#         output = model2(image)
#         probabilities = torch.nn.functional.softmax(output[0], dim=0)
#         predicted_idx = torch.argmax(probabilities).item()
#         confidence = probabilities[predicted_idx].item()
#
#     response_data = {
#         "class": class_names[predicted_idx],
#         "confidence": round(confidence * 100, 2),
#     }
#     return jsonify(response_data)
#
# # Flask 서버 실행
# if __name__ == "__main__":
#     app.run(debug=True)