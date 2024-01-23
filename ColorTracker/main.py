import cv2
import numpy as np

colors = [
    # {"label": "Red", "lower": np.array([0, 100, 100]), "upper": np.array([10, 255, 255]), "color_code": (0, 0, 255)},
    {"label": "Blue", "lower": np.array([100, 100, 100]), "upper": np.array([140, 255, 255]), "color_code": (255, 0, 0)},
    # {"label": "Yellow", "lower": np.array([20, 100, 100]), "upper": np.array([30, 255, 255]), "color_code": (0, 255, 255)}
]

def detect_color(frame, color_data):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = np.zeros_like(frame[:,:,0])  # Use only one channel

    best_contour, best_area = None, 0

    for color_info in color_data:
        lower, upper, label, color_code = color_info["lower"], color_info["upper"], color_info["label"], color_info["color_code"]
        
        color_mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        mask += color_mask

        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > best_area:
                best_contour = contour
                best_area = area

    return mask, best_contour, best_area

def determine_position(frame_width, cx):
    if cx < frame_width // 3:
        return "Kiri"
    elif cx > 2 * frame_width // 3:
        return "Kanan"
    else:
        return "Tengah"

def draw_regions(frame, left_region, center_region, best_contour, label, color_code):
    cv2.rectangle(frame, left_region[0], left_region[1], (0, 0, 255), 2)    # Red for left
    cv2.rectangle(frame, center_region[0], center_region[1], (0, 0, 255), 2)  # Red for center

    if best_contour is not None:
        M = cv2.moments(best_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 10, color_code, -1)
            position = determine_position(frame.shape[1], cx)
            cv2.putText(frame, f"{label} - {position}", (cx - 60, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_code, 2)

def main():
    cap = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Gagal membaca frame, pastikan webcam terhubung.")
                break

            height, width, _ = frame.shape
            left_region = [(width // 3, 0), (width // 3, height)]
            center_region = [(2 * width // 3, 0), (2 * width // 3, height)]

            mask, best_contour, best_area = detect_color(frame, colors)

            # Draw regions using the active color from the colors array
            draw_regions(frame, left_region, center_region, best_contour, colors[0]["label"], colors[0]["color_code"])

            cv2.imshow("Color Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
