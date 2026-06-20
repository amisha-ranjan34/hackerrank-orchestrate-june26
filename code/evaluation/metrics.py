def classification_metrics(
        y_true,
        y_pred
):

    return {

        "accuracy":
            accuracy_score(
                y_true,
                y_pred
            ),

        "precision":
            precision_score(
                y_true,
                y_pred,
                average="macro",
                zero_division=0
            ),

        "recall":
            recall_score(
                y_true,
                y_pred,
                average="macro",
                zero_division=0
            ),

        "f1":
            f1_score(
                y_true,
                y_pred,
                average="macro",
                zero_division=0
            )
    }
    
    
    
def get_confusion_matrix(
        y_true,
        y_pred
):

    return confusion_matrix(
        y_true,
        y_pred
    )
    
    
    
def estimate_cost(

        num_claims,

        avg_input_tokens=1200,

        avg_output_tokens=200,

        input_price=0.0004,

        output_price=0.0016

):

    input_cost = (

        num_claims
        *
        avg_input_tokens
        / 1000

    ) * input_price

    output_cost = (

        num_claims
        *
        avg_output_tokens
        / 1000

    ) * output_price

    return round(
        input_cost + output_cost,
        4
    )
    
    
    
    
    
def estimate_runtime(

        num_claims,

        avg_time_per_claim=5

):

    total_seconds = (

        num_claims
        *
        avg_time_per_claim

    )

    return {

        "seconds": total_seconds,

        "minutes": total_seconds / 60

    }