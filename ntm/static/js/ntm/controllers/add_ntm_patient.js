angular.module('opal.controllers').controller('AddNtmPatientCtrl',
  function(step, scope, episode){
    if(!scope.editing.ntm_symptom){
      scope.editing.ntm_symptom = {};
      scope.editing.ntm_symptom.symptoms  = [];
    }

    if(!scope.editing.ntm_symptom.symptoms){
      scope.editing.ntm_symptom.symptoms = [];
    }

    scope.ntmSymptomFields = {
      "breathlessness": "Breathlessness",
      "cough": "Cough",
      "sputum": "Sputum",
      "fatigue": "Fatigue",
      "fevers": "Fevers",
      "night_sweats": "Night Sweats",
      "weight_loss": "Weight Loss",
      "gi_symptoms": "GI Symptoms",
      "haemoptysis": "Haemoptysis",
      "rash": "Rash",
      "lymphadenopathy": "Lymphadenopathy",
      "skin_infection": "Skin Infection",
      "recurrent_chest_infections": "Recurrent Chest Infections"
    };

    scope.ntmSymptom = {};

    var ntmValues = _.keys(scope.ntmSymptomFields);

    column1 = ntmValues.slice(0, ntmValues.length/2);
    column2 = ntmValues.slice(ntmValues.length/2);

    scope.columns = [column1, column2];

    scope.updateNtmSymptoms = function(){
      var symptoms = scope.editing.ntm_symptom.symptoms;

      var relevent = _.intersection(_.values(scope.ntmSymptomFields), symptoms);

      _.each(scope.ntmSymptomFields, function(v, k){
        var toAdd = _.contains(relevent, v);

        if(scope.ntmSymptom[k]){
          scope.ntmSymptom[k] = toAdd;
        }
        else if(!scope.ntmSymptom[k] && toAdd){
          scope.ntmSymptom[k] = toAdd;
        }
      });
    };

    scope.updateNtmSymptoms();

    scope.updateSymptoms = function(symptomField){
      var symptoms = scope.editing.ntm_symptom.symptoms || [];

      var symptomValue = scope.ntmSymptomFields[symptomField];
      var inSymptoms = _.find(symptoms, function(x){
         return x === symptomValue;
      });
      var toAdd = scope.ntmSymptom[symptomField];

      if(!inSymptoms && toAdd){
        symptoms.push(symptomValue);
      }
      else if(inSymptoms && !toAdd){
        symptoms = _.filter(symptoms, function(x){
            return x !== symptomValue;
        });

        scope.editing.ntm_symptom.symptoms = symptoms;
      }
    };

    scope.preSave = function(editing){
      if(!scope.editing.ntm_symptom.symptoms.length){
         delete editing.ntm_symptom;
      }
    };
});
