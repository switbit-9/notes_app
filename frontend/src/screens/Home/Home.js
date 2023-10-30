import React, { useEffect } from "react";
import { Text, View } from "react-native";
import { useDispatch, useSelector } from "react-redux";
import AppLoader from "../../components/AppLoader/AppLoader";
import InputNotes from "../../components/CreateNote/CreateNotes";
import Posts from "../../components/Posts/Posts";
import { getNotesList } from "../../store/notes/actions";
import ErrorPage from "../Error/Error";


function Home({ navigation }) {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getNotesList());
  }, []);

  const { list, isLoading, error } = useSelector((state) => state.notes);
  // const new_state = useSelector((state) => state.notes);
  // const {list:data } = new_state
  // console.log(data)

  return (
    <View style={{ flex: 1 }}>
      <Text
        style={{
          fontSize: 30,
          fontWeight: "bold",
          textAlign: "center",
          margin: 10,
        }}
      >
        Notes App
      </Text>
      {error && <ErrorPage />}
      <InputNotes />
      {!error && !isLoading && <Posts data={list} />}
      {!error && isLoading && <AppLoader />}
    </View>
  );
}

export default Home;
