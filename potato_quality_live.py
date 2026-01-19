import cv2
import numpy as np

# Skin Texture Check using Laplacian Variance

def check_skin_texture(gray_img, threshold=10):
 
    laplacian_var = cv2.Laplacian(gray_img, cv2.CV_64F).var()
    return laplacian_var > threshold

def detect_sprouts(gray_img, main_contour, max_sprouts=3):
        mask = np.zeros_like(gray_img)
    cv2.drawContours(mask, [main_contour], -1, 255, -1)

    masked_gray = cv2.bitwise_and(gray_img, gray_img, mask=mask)

    _, thresh = cv2.threshold(
        masked_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    sprouts = 0
    for c in contours:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)

        if 100 < area < 2000 and h < 80 and w < 80:
            sprouts += 1

    return sprouts <= max_sprouts

def analyze_potato_live(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return frame

    main_contour = max(contours, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(main_contour)
    area = cv2.contourArea(main_contour)

    aspect_ratio = w / h if h != 0 else 0

    hull = cv2.convexHull(main_contour)
    hull_area = cv2.contourArea(hull)
    solidity = area / hull_area if hull_area != 0 else 0

    extent = area / (w * h) if (w * h) != 0 else 0

    # Shape Validation
    shape_ok = (
        0.5 < aspect_ratio < 2.5 and
        solidity > 0.65 and
        extent > 0.5
    )

    texture_ok = check_skin_texture(gray)
    sprouts_ok = detect_sprouts(gray, main_contour)

    result = "ACCEPTED" if all([shape_ok, texture_ok, sprouts_ok]) else "REJECTED"

    color = (0, 255, 0) if result == "ACCEPTED" else (0, 0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Draw Results
    cv2.drawContours(frame, [main_contour], -1, color, 2)

    cv2.putText(frame, f"Result: {result}", (10, 30),
                font, 0.8, color, 2)

    cv2.putText(frame, f"Aspect Ratio: {aspect_ratio:.2f}", (10, 60),
                font, 0.6, (255, 0, 100), 2)

    cv2.putText(frame, f"Solidity: {solidity:.2f}", (10, 90),
                font, 0.6, (255, 0, 100), 2)

    cv2.putText(frame, f"Extent: {extent:.2f}", (10, 120),
                font, 0.6, (255, 0, 100), 2)

    cv2.putText(frame, f"Skin Texture OK: {texture_ok}", (10, 150),
                font, 0.6, (255, 0, 100), 2)

    cv2.putText(frame, f"Sprouts OK: {sprouts_ok}", (10, 180),
                font, 0.6, (255, 0, 100), 2)

    return frame

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Camera not accessible")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        analyzed_frame = analyze_potato_live(frame)
        cv2.imshow("Live Potato Quality Check", analyzed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

