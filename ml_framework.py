"""Synthetic-data demonstration of supportive learning follow-up prioritisation.
Not a clinical tool, employee assessment, or validated prediction system.
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split

FEATURES = ['completion_pct','days_since_activity','engagement_pct','confidence_pct',
            'accommodation_pct','stress_pct','session_change_pct']

def make_synthetic_data(n=1500, seed=42):
    rng = np.random.default_rng(seed)
    X = np.column_stack([
        rng.uniform(10, 100, n), rng.integers(0, 29, n),
        rng.uniform(20, 100, n), rng.uniform(20, 100, n),
        rng.uniform(15, 100, n), rng.uniform(5, 90, n),
        rng.uniform(-55, 35, n)
    ])
    # Artificial ground-truth rule for an educational demo ONLY.
    score = (0.035 * (70-X[:,0]) + 0.14 * (X[:,1]-7)
             + 0.025 * (65-X[:,2]) + 0.020 * (60-X[:,4])
             + 0.014 * (X[:,5]-40) + 0.012 * (-X[:,6]))
    p = 1/(1+np.exp(-np.clip(score/2.5,-30,30)))
    y = (rng.random(n) < p).astype(int)
    return X, y

def train_demo_model():
    X,y = make_synthetic_data()
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model=RandomForestClassifier(n_estimators=120,max_depth=7,min_samples_leaf=8,
                                 class_weight='balanced',random_state=42)
    model.fit(X_train,y_train)
    probabilities=model.predict_proba(X_test)[:,1]
    return model, {'synthetic_test_auc':roc_auc_score(y_test,probabilities),
                   'report':classification_report(y_test,model.predict(X_test),zero_division=0)}

def suggest_followup(model, completion_pct, days_since_activity, engagement_pct,
                     confidence_pct, accommodation_pct, stress_pct, session_change_pct):
    x=np.array([[completion_pct,days_since_activity,engagement_pct,confidence_pct,
                 accommodation_pct,stress_pct,session_change_pct]],dtype=float)
    probability=float(model.predict_proba(x)[0,1])
    # The score indicates similarity to synthetic labels, NOT actual employee risk.
    return {'synthetic_followup_score':round(probability,3),
            'suggestion':('Offer a voluntary, supportive check-in' if probability >= .65
                          else 'Continue routine supportive learning follow-up')}

if __name__=='__main__':
    model,metrics=train_demo_model()
    print('Synthetic-only model | holdout ROC-AUC:',round(metrics['synthetic_test_auc'],3))
    print(metrics['report'])
    example=suggest_followup(model,54,14,50,58,45,64,-22)
    print('Example fictional learner:',example)
