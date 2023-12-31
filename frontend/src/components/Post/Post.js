import React, { useState } from "react";
import { TouchableOpacity, View } from "react-native";
import { Button, Card, Text } from "react-native-paper";
import { useDispatch } from "react-redux";
import { deleteNote, updateNote } from "../../store/notes/actions";
import InputNote from "../InputNotes/InputNote";
import styles from "./styles";

function Post({ item }) {
  const dispatch = useDispatch();
  const [isSaveMode, setIsSaveMode] = useState(false);
  const [isFullTextVisible, setIsFullTextVisible] = useState(false);

  const onDeletehandler = () => {
    dispatch(deleteNote(item.id_));
    // dispatch(getNotesList());
  };

  const onPressUpdate = (title, description) => {
    const payload = {
      body: {
        title,
        description,
      },
      id: item.id_,
    };
    dispatch(updateNote(payload));
    setIsSaveMode(false);
  };

  const cardContentRead = (
    <>
      <Text style={{ fontSize: 20 }}>{item.title}</Text>
      {isFullTextVisible && <Text>{item.description}</Text>}
      <TouchableOpacity
        onPress={() => setIsFullTextVisible(!isFullTextVisible)}
      >
        <Text style={styles.toggleButton}>
          {isFullTextVisible ? "Hide" : "Show More"}
        </Text>
      </TouchableOpacity>
      <Button icon="update" onPress={() => setIsSaveMode(true)}>
        Edit
      </Button>
    </>
  );

  const cardContentUpdate = (
    <InputNote
      item={item}
      button={{ icon: "update", title: "Save", mode: "" }}
      onPress={onPressUpdate}
    />
  );

  const cardContent = isSaveMode ? cardContentUpdate : cardContentRead;

  return (
    <View>
      <Card style={styles.cardStyle}>
        {cardContent}
        <Button icon="delete" onPress={onDeletehandler}>
          Delete
        </Button>
      </Card>
    </View>
  );
}

export default Post;
