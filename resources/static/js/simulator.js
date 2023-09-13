const callInitializeDemoData = () => {
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "/simulator-api/demo-data");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 204) {
            alert("Datos inicializados correctamente.");
        }
    }

    xhr.send();
}

const callCallWebhookForOneTime = () => {
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "/simulator-api/transactions/for-one-time-expense");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 204) {
            alert("Transacción registrada correctamente.");
        }
    }

    xhr.send();
}

const callCallWebhookForRecurring = () => {
    const xhr = new XMLHttpRequest();

    xhr.open("POST", "/simulator-api/transactions/for-recurring-expense");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 204) {
            alert("Transacción registrada correctamente.");
        }
    }

    xhr.send();
}
