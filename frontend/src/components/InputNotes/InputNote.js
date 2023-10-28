import React, { useState } from "react";
import { View } from "react-native";
import { Button, TextInput } from "react-native-paper";
import { useDispatch, useSelector } from "react-redux";
import {
  createNote,
  getNotesList,
  updateNote,
} from "../../store/notes/actions";
import styles from "./styles";

function InputNote({ item, button, actionType }) {
  const dispatch = useDispatch();
  const initialTitle = item?.title ? item.title : "";
  const initialDescription = item?.description ? item.description : "";

  const [title, setTitle] = useState(initialTitle);
  const [description, setDescription] = useState(initialDescription);


  const onPressHandler = () => {
    body = {
      title: title,
      description: description,
    };
    body = JSON.stringify(body);
    console.log(body);
    if (actionType === "create") {
      dispatch(createNote(body));
    } else {
        payload = {
            'body' : body, 
            'id' : item.id_
        }
      dispatch(updateNote(payload));
    }
    dispatch(getNotesList());
  };

  return (
    <View>
      <TextInput
        style={{ fontSize: 20 }}
        label="Title"
        value={title}
        onChangeText={(text) => setTitle(text)}
      />
      <TextInput
        label="Description"
        multiline
        value={description}
        onChangeText={(text) => setDescription(text)}
      />
      <Button
        style={button.style}
        icon={button.icon}
        mode={button.mode}
        onPress={onPressHandler}
      >
        {button.title}
      </Button>
    </View>
  );
}

export default InputNote;
