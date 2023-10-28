import React, { useEffect } from "react";
import { View } from "react-native";
import { useDispatch, useSelector } from "react-redux";
import AppLoader from "../../components/AppLoader/AppLoader";
import InputNotes from "../../components/CreateNote/CreateNotes";
import Posts from "../../components/Posts/Posts";
import { getNotesList } from "../../store/notes/actions";
import ErrorPage from "../Error/Error";


function Home({ navigation }) {
  const dispatch = useDispatch();
  const error = useSelector((state) => state.notes.error);
  useEffect(() => {
    dispatch(getNotesList());
  }, []);

  const data = useSelector((state) => state.notes.list);
  const isLoading = useSelector((state) => state.notes.isLoading);

  return (
    <View style={{ flex: 1 }}>
      {error && <ErrorPage />}
      <InputNotes />
      {!error && !isLoading && <Posts data={data} />}
      {!error && isLoading && <AppLoader />}
    </View>
  );
}

export default Home;
