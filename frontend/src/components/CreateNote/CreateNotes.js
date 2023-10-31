import React, { useState } from "react";
import { View } from "react-native";
import { Button } from "react-native-paper";
import { useDispatch } from "react-redux";
import InputNote from "../InputNotes/InputNote";
import { createNote } from "../../store/notes/actions";

function InputNotes() {
  const dispatch = useDispatch();
  const [showForm, setShowForm] = useState(false);

  const onPressCreate = (title, description) => {
    const body = {
      title: title,
      description: description,
    };
    dispatch(createNote(body));
  };
  return (
    <View>
      {!showForm && (
        <Button
          mode="contained"
          icon="pencil"
          onPress={() => setShowForm(true)}
        >
          Create Note
        </Button>
      )}
      {showForm && (
        <InputNote
          button={{
            title: "Create",
            style: { margin: 10 },
            icon: "pencil",
            mode: "contained",
          }}
          onPress={onPressCreate}
        />
      )}
    </View>
  );
}

export default InputNotes;
