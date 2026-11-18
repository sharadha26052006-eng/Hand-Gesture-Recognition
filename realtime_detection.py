
import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# Initialize webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("ERROR: Webcam not detected!")
    hands.close()
    exit()

print("Hand Gesture Recognition Started!")
print("Press Q to quit.")

# Gesture recognition function
def recognize_gesture(hand, handedness):

    lm = hand.landmark

    # Determine hand direction
    is_right = handedness == "Right"

    # Thumb detection
    if is_right:
        thumb = lm[4].x < lm[3].x
    else:
        thumb = lm[4].x > lm[3].x

    # Other finger detection
    index = lm[8].y < lm[6].y
    middle = lm[12].y < lm[10].y
    ring = lm[16].y < lm[14].y
    pinky = lm[20].y < lm[18].y

    fingers = [index, middle, ring, pinky]

    # Classify gestures
    if all(fingers) and thumb:
        return "OPEN PALM"

    elif not any(fingers) and not thumb:
        return "FIST"

    elif index and middle and not ring and not pinky:
        return "VICTORY"

    elif index and not middle and not ring and not pinky:
        return "POINTING"

    elif thumb and not any(fingers):
        return "THUMBS UP"

    else:
        return "UNKNOWN"

# Main webcam loop
try:
    while True:

        ret, frame = cap.read()

        if not ret:
            print("ERROR: Cannot read webcam frame!")
            break

        # Mirror webcam
        frame = cv2.flip(frame, 1)

        # Convert image
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process hand
        results = hands.process(rgb)

        gesture = "NO HAND DETECTED"

        if results.multi_hand_landmarks:

            for i, hand in enumerate(results.multi_hand_landmarks):

                mp_draw.draw_landmarks(
                    frame,
                    hand,
                    mp_hands.HAND_CONNECTIONS
                )

                handedness = "Right"

                if results.multi_handedness:
                    handedness = results.multi_handedness[i].classification[0].label

                gesture = recognize_gesture(hand, handedness)

        # Display gesture
        color = (0, 255, 0) if gesture != "NO HAND DETECTED" else (0, 0, 255)

        cv2.rectangle(frame, (0, 0), (640, 80), (30, 30, 30), -1)

        cv2.putText(
            frame,
            "HAND GESTURE RECOGNITION",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Gesture: " + gesture,
            (15, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        cv2.imshow("SkillCraft - Hand Gesture Recognition", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    cap.release()
    hands.close()
    cv2.destroyAllWindows()
    print("Webcam released successfully.")
