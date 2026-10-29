
from data_cleaning import clean_data
from train_model import train_model
from test_model import test_model


def main():

    print("\nSTEP 1: CLEAN DATASET")
    clean_data()

    print("\nSTEP 2: TRAIN CNN MODEL")
    train_model()

    print("\nSTEP 3: TEST CNN MODEL")
    test_model()

    print("\nPROJECT COMPLETED SUCCESSFULLY!")
    print("Start the interface using:")
    print("streamlit run app.py")


if __name__ == "__main__":
    main()
