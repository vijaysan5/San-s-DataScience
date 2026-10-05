import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import classification_report, confusion_matrix


# ============================================================
# 1. DATASET PATH
# ============================================================

DATASET_PATH = r"D:\karthikeyan\NOTES\AI\ART\cnn\dataset"

TRAIN_DIR = os.path.join(DATASET_PATH, "train")
TEST_DIR = os.path.join(DATASET_PATH, "test")


# ============================================================
# 2. PARAMETERS
# ============================================================

IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 30


# ============================================================
# 3. DATA AUGMENTATION + TRAIN/VALIDATION SPLIT
# ============================================================

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,

    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)


train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True
)


validation_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation",
    shuffle=False
)


# ============================================================
# 4. TEST DATA
# ============================================================

test_datagen = ImageDataGenerator(
    rescale=1.0 / 255
)


test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)


# ============================================================
# 5. CHECK CLASSES
# ============================================================

class_names = list(train_generator.class_indices.keys())

print("Classes:")
for i, name in enumerate(class_names):
    print(i, ":", name)

NUM_CLASSES = len(class_names)

print("\nNumber of classes:", NUM_CLASSES)
print("Training images:", train_generator.samples)
print("Validation images:", validation_generator.samples)
print("Test images:", test_generator.samples)


# ============================================================
# 6. BUILD CNN MODEL
# ============================================================

model = models.Sequential([

    # Input
    layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3)),

    # CNN Block 1
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    # CNN Block 2
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    # CNN Block 3
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    # CNN Block 4
    layers.Conv2D(256, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    # Regularization
    layers.Dropout(0.5),

    # Flatten
    layers.Flatten(),

    # Fully Connected Layer
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.5),

    # Output
    layers.Dense(NUM_CLASSES, activation="softmax")
])


# ============================================================
# 7. MODEL SUMMARY
# ============================================================

model.summary()


# ============================================================
# 8. COMPILE MODEL
# ============================================================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# ============================================================
# 9. CALLBACKS
# ============================================================

callbacks = [

    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=7,
        restore_best_weights=True
    ),

    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=3,
        min_lr=1e-7
    ),

    tf.keras.callbacks.ModelCheckpoint(
        "best_car_cnn.keras",
        monitor="val_accuracy",
        save_best_only=True
    )
]


# ============================================================
# 10. TRAIN CNN
# ============================================================

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS,
    callbacks=callbacks
)


# ============================================================
# 11. TEST ACCURACY
# ============================================================

test_loss, test_accuracy = model.evaluate(test_generator)

print("\nTest Loss:", test_loss)
print("Test Accuracy:", test_accuracy)


# ============================================================
# 12. TRAINING / VALIDATION ACCURACY GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    history.history["accuracy"],
    label="Training Accuracy"
)

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("CNN Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid()

plt.show()


# ============================================================
# 13. TRAINING / VALIDATION LOSS GRAPH
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    history.history["loss"],
    label="Training Loss"
)

plt.plot(
    history.history["val_loss"],
    label="Validation Loss"
)

plt.title("CNN Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid()

plt.show()


# ============================================================
# 14. PREDICTIONS
# ============================================================

test_generator.reset()

predictions = model.predict(test_generator) 

predicted_classes = np.argmax(
    predictions,
    axis=1
)

true_classes = test_generator.classes


# ============================================================
# 15. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:\n")

print(
    classification_report(
        true_classes,
        predicted_classes,
        target_names=class_names
    )
)


# ============================================================
# 16. CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    true_classes,
    predicted_classes
)

plt.figure(figsize=(10, 8))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    xticklabels=class_names,
    yticklabels=class_names
     
)

plt.title("CNN Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("True Class")

plt.show()


# ============================================================
# 17. SAVE FINAL MODEL
# ============================================================

model.save("car_classification_cnn.keras")

print("\nModel saved as car_classification_cnn.keras")