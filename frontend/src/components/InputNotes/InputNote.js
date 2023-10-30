import React, { useState } from "react";
import { View } from "react-native";
import { Button, TextInput } from "react-native-paper";

function InputNote({ item, button, onPress }) {
  const [title, setTitle] = useState(item?.title ? item.title : "");
  const [description, setDescription] = useState(
    item?.description ? item.description : ""
  );

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
        onPress={() => onPress(title, description)}
      >
        {button.title}
      </Button>
    </View>
  );
}

export default InputNote;
