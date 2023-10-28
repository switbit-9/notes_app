import React, { useState } from "react";
import { View } from "react-native";
import InputNote from "../InputNotes/InputNote";
import { Button } from "react-native-paper";
import styles from "../Posts/styles";
function InputNotes() {
  const [showForm, setShowForm] = useState(false)


  return (
    <View>
      {!showForm && <Button mode="contained" icon='pencil' onPress={() => setShowForm(true)}>Create Note</Button>}
      {showForm && <InputNote
        actionType={"create"}
        button={{
          title: "Create",
          style: { margin: 10 },
          icon: "pencil",
          mode: "contained",
        }}
      />}
    </View>
  );
}

export default InputNotes;
