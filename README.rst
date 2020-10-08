**TOMER: Temperature Optima for Enzymes with Resampling**
------------------------------------------------------------

TOMER is a Python package for predicting the catalytic optimum temperature (Topt) of enzymes with machine learning. TOMER was trained with a bagging ensemble on a dataset of 2,917 proteins. To prevent large error on the prediction of higher temperature values, resampling strategies were applied to mitigate the effects of the imbalanced distribution of the dataset. Code for design of TOMER can be found `here <https://github.com/jafetgado/tomerdesign>`_.

Citation
----------
If you find TOMER useful, please cite:

* Gado, J.E., Beckham, G.T., and Payne, C.M (2020). Improving enzyme optimum temperature prediction with resampling strategies and ensemble learning. *J. Chem. Inf. Model.* 60(8), 4098-4107.


Installation
-------------
Install with pip

.. code:: shell-session

    pip install tomer

Or from source (preferred). Using a virtual environment is recommended.

.. code:: shell-session

    git clone https://github.com/jafetgado/resreg.git
    cd tomer
    pip install -r requirements.txt
    python setup.py install



Prerequisites
----------------
(version used in this work)

1. Python 3 (3.6.6)
2. Scikit-learn (0.21.2)
3. Numpy (1.14.2)
4. Pandas (0.24.1)
5. Joblib (0.13.2)


Usage
-----
There are two main functions in TOMER for predicting the enzyme optimum temperature: ``pred_seq_topt``, which predicts optimum temperature of a single protein sequence (string), and ``pred_fasta_topt``, which predicts the optimum temperatures of protein sequences in a fasta file. To use these functions, you have to specify the optimal growth temperature (OGT) of the source organism of the protein. If the OGT is not known, a prediction may be obtained using `TOME <https://github.com/EngqvistLab/Tome>`_.



Examples
----------
.. code:: python

    import tomer

    # Predict optimum temperature of a single sequence.
    sequence = '''MKKQVVEVLVEGGKATPGPPLGPAIGPLGLNVKQVVDKINEATKEFAGMQVPVKIIV
                  DPVTKQFEIEVGVPPTSQLIKKELGLEKGSGEPKHNIVGNLTMEQVIKIAKMKRSQML
                  ALTLKAAAKEVIGTALSMGVTVEGKDPRIVQREIDEGVYDELFEKAEKE'''
    ogt = 95
    y_pred, y_err = tomer.pred_seq_topt(sequence, ogt)

    print(y_pred)   # predicted optimum temperature
    82.415

    print(y_err)    # Standard error of prediction (over 100 base learners in ensemble)
    2.0913518953060004

    # Predict optimum temperatures of sequences in fasta file
    fasta_file = 'test/sequences.fasta'
    ogt_file = 'test/ogts.txt'
    df = tomer.pred_fasta_topt(fasta_file, ogt_file) # returns dataframe

    print(df)
       Sequence  Topt    Std err
    0   P43408  79.345   1.53561
    1   Q97X08  81.705  0.442442
    2   F8A9V0   76.37   1.16195

